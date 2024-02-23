// enums are a type that may be one of a few variants
// any variant valid as a struct, is also valid as an enum

// classifies a web event
// names and types together specify a variant
enum WebEvent {
    // an enum may be unit like
    PageLoad,
    PageUnload,
    // like a tuple struct
    KeyPress(char),
    Paste(String),
    // or c-like structs
    Click {x: i64, y: i64},
}

// takes a WebEvent and returns nothing
fn _inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page loaded"),
        WebEvent::PageUnload => println!("page unloaded"),
        // destructure from inside the enum
        WebEvent::KeyPress(c) => println!("pressed '{c}'"),
        WebEvent::Paste(s) => println!("pasted '{s}'"),
        WebEvent::Click { x, y } => println!("clicked at x={x}, y={y}"),
    }
}

// enums can be given an alias of which there variants can be referred
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// creates a type alias
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

// most common place to create an alias is in the impl block of an enum
// the `Self` keyword is an alias of the enum
impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn _run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    let pasted = WebEvent::Paste("my text".to_owned());
    let click = WebEvent::Click { x: 20, y: 80 };
    let load = WebEvent::PageLoad;
    let unload = WebEvent::PageUnload;

    _inspect(pressed);
    _inspect(pasted);
    _inspect(click);
    _inspect(load);
    _inspect(unload);

    // refer to the the enum with a really long name using its alias
    let _x = Operations::Add;
    println!("4 + 5 = {}", _x._run(4, 5));
    println!("4 - 5 = {}", Operations::Subtract._run(4, 5));
}

