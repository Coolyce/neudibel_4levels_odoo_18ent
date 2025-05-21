import { beforeEach, describe, expect, test } from "@odoo/hoot";
import { getService, makeMockEnv } from "@web/../tests/web_test_helpers";

describe.current.tags("headless");

let titleService;

beforeEach(async () => {
    await makeMockEnv();
    titleService = getService("title");
});

test("simple title", () => {
    titleService.setParts({ one: "My4levels" });
    expect(titleService.current).toBe("My4levels");
});

test("add title part", () => {
    titleService.setParts({ one: "My4levels", two: null });
    expect(titleService.current).toBe("My4levels");
    titleService.setParts({ three: "Import" });
    expect(titleService.current).toBe("My4levels - Import");
});

test("modify title part", () => {
    titleService.setParts({ one: "My4levels" });
    expect(titleService.current).toBe("My4levels");
    titleService.setParts({ one: "Zopenerp" });
    expect(titleService.current).toBe("Zopenerp");
});

test("delete title part", () => {
    titleService.setParts({ one: "My4levels" });
    expect(titleService.current).toBe("My4levels");
    titleService.setParts({ one: null });
    expect(titleService.current).toBe("4levels");
});

test("all at once", () => {
    titleService.setParts({ one: "My4levels", two: "Import" });
    expect(titleService.current).toBe("My4levels - Import");
    titleService.setParts({ one: "Zopenerp", two: null, three: "Sauron" });
    expect(titleService.current).toBe("Zopenerp - Sauron");
});

test("get title parts", () => {
    expect(titleService.current).toBe("");
    titleService.setParts({ one: "My4levels", two: "Import" });
    expect(titleService.current).toBe("My4levels - Import");
    const parts = titleService.getParts();
    expect(parts).toEqual({ one: "My4levels", two: "Import" });
    parts.action = "Export";
    expect(titleService.current).toBe("My4levels - Import"); // parts is a copy!
});
