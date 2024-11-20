import { cascLib } from "./libs";

test("Testing export file", () => {
  console.log(cascLib);
  expect(cascLib._test_greet()).toBe("I am CASCLIB!!");
});
