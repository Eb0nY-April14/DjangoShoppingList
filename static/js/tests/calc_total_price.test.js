// const { TestWatcher } = require("@jest/core")
const change = require("../calc_total_price")

describe("totalPrice", () => {
    describe("Change function", () => {
        test("should return 59.96 for 14.99 * 4", () => {
            expect(change(14.99,4)).toBe(59.96);
        })
    });
});