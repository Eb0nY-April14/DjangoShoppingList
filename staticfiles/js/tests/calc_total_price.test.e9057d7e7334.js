// const { TestWatcher } = require("@jest/core")
const multiply = require("../calc_total_price")

describe("totalPrice", () => {
    describe("Multiply function", () => {
        test("should return 59.96 for 14.99 * 4", () => {
            expect(multiply(14.99,4)).toBe(59.96);
        })
    });
});