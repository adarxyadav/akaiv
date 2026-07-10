#!/usr/bin/env node
// Rerunnable check for two-doors.html's DOM-free scoring block.
// It evaluates the pure-logic section of the shipped page itself (no copy),
// so the page and its check can't drift apart. Exit 0 = pass.
import { readFileSync } from "node:fs";
import assert from "node:assert/strict";

const html = readFileSync(new URL("../two-doors.html", import.meta.url), "utf8");
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const pure = script.slice(0, script.indexOf("const $"));
const { norm, scoreRecall, scoreRecog, shuffle, SETS } =
  new Function(`${pure}; return { norm, scoreRecall, scoreRecog, shuffle, SETS };`)();

const targets = SETS[0].targets;

assert.equal(norm("Violins,"), "violin"); // case, punctuation, trailing s
assert.equal(scoreRecall("Violins, CACTUS umbrella umbrella pigeonn", targets), 3); // dupes count once, typo misses
assert.equal(scoreRecall("", targets), 0);
assert.deepEqual(scoreRecog(["violin", "guitar", "anchor"], targets), { hits: 2, alarms: 1 });
for (const s of SETS) assert.equal(new Set(s.targets.concat(s.lures)).size, 16); // no dupes → every grid button unambiguous
assert.deepEqual(shuffle(targets).slice().sort(), targets.slice().sort()); // permutation, nothing lost
assert.deepEqual(targets, SETS[0].targets); // shuffle didn't mutate its input

console.log("two-doors scoring: all checks pass");
