# Notes
## TypeScript
``` ts
// Basic type annotations
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// Type inference (TypeScript infers the type)
let city = "Sydney"; // TypeScript knows this is a string

// Arrays
let numbers: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// Objects
let person: { name: string; age: number } = {
  name: "Alice",
  age: 30
};

// Union types (multiple possible types)
let id: string | number = "abc123";
id = 42; // Also valid

// Any type (opts out of type checking)
let data: any = "hello";
data = 42; // No error

// Const variables (immutable reference)
const PI: number = 3.14159;
```