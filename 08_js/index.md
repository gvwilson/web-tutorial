# An Hour of JavaScript

-   Install [deno][deno] for command-line JavaScript

## Variables, Types, and Control Flow

``` { .js #console_log.js }
console.log('hello, world');
```

-   Run program as `deno run program.js`
-   `console` is a built-in module
-   Use the same dotted notation as Python
-   Trailing semi-colon is no longer required but commonly used

``` { .js #loop_if_truthiness.js }
const values = [0, 1, '', 'text', undefined, null, [], [2, 3]];
for (const val of values) {
    const type = typeof val;
    if (val) {
        console.log(`val '${val}' of type ${type} seems true`);
    } else {
        console.log(`val '${val}' of type ${type} seems false`);
    }
}
```

-   `const` defines a constant
-   The array contents aren't constant: the reference is
-   `for…in` loops over the contents of an array
-   Use `for…of` to loop over indices
-   Parentheses are required
-   `typeof` is an operator not a function, and returns a string
-   `if` / `else if` / `else` work as expected
-   Use back-quotes and `${…}` for string interpolation
-   JavaScript considers an empty array to be truthy
-   Always use `===` (triple equals) and `!==` for equality
-   Otherwise JavaScript does some strange type conversions

## Objects

``` { .js #object_access.js }
const person = {
    'staff_id': 31,
    'personal': 'Loan',
    'family': 'Nguyen'
};
console.log(`personal: ${person.personal}`);
console.log(`family: ${person['family']}`);
```

-   JavaScript objects are (kind of) like Python dictionaries
-   Create so many of these that keys don't have to be quoted

``` { .js #object_unquoted.js }
const person = {
    staff_id: 31,
    personal: 'Loan',
    family: 'Nguyen'
};
console.log(`personal: ${person.personal}`);
```

-   Can use variables' names and values to construct objects

``` { .js #object_variables_as_fields.js }
const staff_id = 31;
const personal = 'Loan';
const family = 'Nguyen';
const person = {staff_id, personal, family};
console.log(`person: ${JSON.stringify(person)}`);
```

-   `JSON` is another built-in module
-   Its `stringify` function does what its name suggests
-   Without this, `person` is displayed as `[Object object]`

## Functions

``` { .js #function_def_and_call.js }
function limits (values) {
  if (!values.length) {
    return [undefined, undefined];
  }
  let low = values[0];
  let high = values[0];
  for (let v of values) {
    if (v < low) {
        low = v;
    }
    if (v > high) {
        high = v;
    }
  }
  return [low, high]
}

const result = limits([1, -3, 2, 7]);
console.log(result);
```

-   `let` introduces a variable
-   The older `var` is still sometimes used
-   Functions take parameters, create a scope, etc.

``` { .js #arrow_function.js }
const largest = (left, right) => {
    if (left < right) {
        return left;
    } else {
        return right;
    }
}

console.log(`largest(3, 5) is ${largest(3, 5)}`);
```

-   A function is just another kind of object
-   Can define using arrow notation and then assign to a variable
-   Handy in a language that uses lots of little functions

``` { .js #higher_order_func.js }
const values = [1, -3, 5, -7];

const is_positive = values.map((v) => v >= 0);
console.log(`is_positive: ${is_positive}`);

const keep_positive = values.filter(v => v >= 0);
console.log(`keep_positive: ${keep_positive}`);

const print_positive = values.forEach(v => {
    if (v >= 0) {
        console.log(v);
    }
});
```

## Asynchronous Operations

``` { .js #promises.js }
const middle = Deno.readTextFile("middle.txt");
console.log(`middle is ${middle}`);
middle.then(value => {
    console.log(`middle.then is ${value}`);
});
```

-   A promise represents a delayed operation
-   Use `.then` method to tell JavaScript what to do when a value becomes available
    -   Use this a lot in web programming so that the browser won't freeze up

``` { .js #await.js }
const value = await Deno.readTextFile("left.txt");
console.log(`left value is ${value}`);
```

-   `await` makes asynchronous operations more readable

[deno]: https://deno.com/
