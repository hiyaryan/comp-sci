// `use` declaration can be used so manual scoping isn't needed

#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // explicitly `use` each name so they're available without manual scoping.
    use crate::Status::{Poor, Rich};
    // automatically `use` each name inside `Work`.
    use crate::Work::*;

    // Equivalent to `Status::Poor`.
    let status = Poor;
    // Equivalent to `Work::Poor`.
    let work = Civilian;

    // match cases did not need to be scoped for the enums below since they
    // are explicitly being `use`d in this function.
    match status {
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }

    match work {
        Civilian => println!("Civilians work!"),
        Soldier => println!("Soldiers fight!"),
    }
}
