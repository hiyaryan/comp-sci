// The `match` Control Flow Construct
// `match` compares a value against a series of patterns and then executes code based on which pattern matches.
// Patterns can be made up of literal values, variable names, wildcards, and many others (see ch 18)

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState), // UsState type added to indicate only Quarters from 1999-2008 may include state designs.
}

// Patterns that Bind to Values
// Match arms can bind to parts of values that match the pattern allowing values from enum variants to be extracted.
#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

// The match expression can return any value (unlike an if that can only return a boolean)
// These expressions are composed of arms that are used to match the returned value of the match expression.
// The code in each arm is an expression that returns a resulting value for the entire match expression.
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        // If there is more than a single expression in an arm {} must be used.
        Coin::Penny => { 
            println!("Lucky penny!");
            1
        },
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => { // variable state is added to the match expression that matches values of variant Coin::Quarter
                                  // when a Coin::Quarter matches, the state variable will bind to the value of that quarter's state.
            println!("State quarter from {:?}!", state);
            25
        },
    }
}

// Matching with Option<T>
// How to get the T out of Option<t>.. use `match`
// This function takes an Option<i32> and if there's a value inside, adds 1 to that value, otherwise, return None.
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}

// Matches Are Exhaustive
// All variants of an enum must be covered in the match expression. This prevents the mistake of using a null value in an operation.
// The following function does not work because None is not covered.
// fn plus_one(x: Option<i32>) -> Option<i32> {
//     match x {
//         Some(i) => Some(i + 1),
//         // None is not handled here so it will result in an error[E0004]: non-exhaustive patterns
//     }
// }

// Catch-all Patterns
// Functions used in example:
fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
fn reroll() {}

fn main() {
    // Example using a matching a coin to Quarter with an Alaska design.
    let quarter = value_in_cents(Coin::Quarter(UsState::Alaska));
    println!("The coin has a value of {}.", quarter);

    // Matching with Option<T>
    let five = Some(5); // Some(5) is a variant of Option<i32>
    let six = plus_one(five); // Match it against Some(i)
    let none = plus_one(None); // Match it against None

    println!("The value of Option<5> is {:?}", five);
    println!("The value of Option<5 + 1> is {:?}", six);
    println!("The value of Option<None> is {:?}", none);

    // Catch-all Patterns and the _ Placeholder
    // Special actions can be taken for some variants of an enum, for all other variants take a default actions.
    let dice_roll = 9; // dice landed on 9
    match dice_roll {
        3 => add_fancy_hat(), // covers values for 3
        7 => remove_fancy_hat(), // covers values for 7
        other => move_player(other), // covers all 'other' values
    }

    // To use a catch-all but not use the value in the catch-all pattern the `_` symbol can be used in place of `other`.
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        _ => reroll(),
    }
    // Above meets the exhaustive requirements because all other values are explicitly being ignored. Any other value
    // not a 3 or 7 has been addressed, it should be ignored.

    // Use the unit value (empty tuple, see ch 3.2) to make nothing happen for rolls other than 3 or 7.
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        _ => (), // empty tuple expresses that nothing should happen for any value not a 3 or 7.
    }

    // For more on patterns and matching, see ch 18.
}