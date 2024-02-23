// linked lists can be implemented using enums
use crate::List::*;

enum List {
    // Cons: Tuple struct that wraps an element and a pointer to the next node
    Cons(u32, Box<List>),
    // Nil: A node that signifies the end of the linked list
    Nil,
}

// Methods can be attached to an enum
impl List {
    // create an empty list
    fn new() -> List {
        // `Nil` has type `List`
        Nil
    }

    // Consume a list and return the same list with a new element at its front
    fn prepend(self, elem: u32) -> List {
        Cons(elem, Box::new(self))
    }

    // return the length of th list
    fn len(&self) -> u32 {
        match *self {
            Cons(_, ref tail) => 1 + tail.len(),
            Nil => 0,
        }
    }

    // return a string representation of the list
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // format returns a heap allocated string instead of printing to the console
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                "Nil".to_string()
            }
        }
    }
}

fn main() {
    // create an empty linked list
    let mut list = List::new();

    // prepend some elements
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // show final state of the list
    println!("linked list has length {}", list.len());
    println!("{}", list.stringify());
}
