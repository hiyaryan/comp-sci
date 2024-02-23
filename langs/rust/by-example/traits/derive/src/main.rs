// provide basic implementation for some traits via the #[derive] attribute
// if more complex behavior is required these traits can be manually implemented

// def. attribute: metadata applied to some module, crate or item.
// - when applied to a whole crate use #![crate_attribute]
// - when applied to a module or item use #[item_attributes]
// see Attributes section of documentation for more information.

// derivable traits
// - Comparison trits: `Eq`, `PartialEq`, `Ord`, `PartialOrd`
// - `Clone`, create `T` from `&T` via a copy
// - `Copy`, give a type 'copy semantics' instead of `move semantics`
// - `Hash`, compute a hash from `&T`
// - `Default`, create an empyt instance from a data type
// - `Debug`, format a value using the {:?} formatter

#[derive(PartialEq, PartialOrd)]
// tuple struct that can be compared
struct Centimeters(f64);

// tuple struct that can be printed
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// tuple struct with no added attributes
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);
    // Error: Doesn't implement `Debug` trait
    // println!("one second {}", _one_second)

    // Error: Doesn't implement the `PartialEq` trait
    // let _this_is_true = (_one_second == _one_second);

    let foot = Inches(12);
    println!("One foot equals {foot:?}");

    let meter = Centimeters(100.0);

    let cmp = 
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("one foot is {cmp} than one meter.");
}
