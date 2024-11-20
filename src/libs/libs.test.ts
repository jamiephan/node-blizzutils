import { cascLib } from "./libs";

test("Testing export file", () => {
  expect(cascLib.casclib()).toBe("I am CASCLIB!!");
});
