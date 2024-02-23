// three types of structs
// tuple struct
// classic C style struct
// field-less structs called unit structs useful for generics

#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// unit struct
struct Unit;

// tuple struct
struct Pair(i32, f32);

#[derive(Debug)]
// struct with two fields
struct Point {
    x: f32,
    y: f32,
}

#[derive(Debug)]
// reuse structs as fields for other structs
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

impl Rectangle {
    fn rect_area(&self) -> f32 {
        // from bottom_right need x
        // from top_left need y
        // A = 2 * (1/2) * x * y = x * y
        let Pair (x_component, y_component) = Pair(self.bottom_right.x as i32, self.top_left.y);
        x_component as f32 * y_component
    }

    // returns a recatngle with the top left corner on the point and bottom right corner corresponding to an f32
    // not sure how this was supposed to work but got the point of the lesson anyway
    fn square(&self, top_left: Point, bottom_right: f32) -> Self {
        Rectangle { top_left, bottom_right: Point { x: bottom_right, y: bottom_right } }
    }
}

fn main() {
    // create strut with field init shorthand
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // print debug struct
    println!("{peter:?}");

    // instantiate a point
    let point: Point = Point { x: 10.3, y: 0.4 };

    // access fields of the point
    println!("point coordinates: ({}, {})", point.x, point.y);

    // make a new point by using struct update syntax to use the fields from another one
    let bottom_right = Point { x: 5.2, ..point };
    // let bottom_right = Point { y: 5.2, ..point}; // base struct must always be the last field
    // let bottom_right = Point { ..point, y: 5.2 }; // error

    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // destructure a struct using let binding
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle  {
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right,
    };

    // instantiate a unit struct
    let _unit = Unit;

    // instantiate tuple struct
    let pair = Pair(1, 0.1);

    // access fields of tuple struct
    println!("pair contains {} and {}", pair.0, pair.1);

    // destructure a tuple struct
    let Pair( integer, decimal ) = pair;
    println!("pair contains {integer} and {decimal}");


    println!("The area of {:?} is {}", _rectangle, _rectangle.rect_area());
    println!("The rectangle {:?} is now square {:?}.", &_rectangle, _rectangle.square(Point { x: 2.0, y: 1.0 }, 2.0));
}