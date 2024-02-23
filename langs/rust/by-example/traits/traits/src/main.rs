// A trait is a collection of methods defined for an unknown type: Self. 
// Traits can access other methods declared in it. 

// Traits can be implemented for any data type.

struct Sheep {
    naked: bool,
    name: &'static str
}

trait Animal {
    // associated function signature
    // `Self` refers to the implementation type
    fn new(name: &'static str) -> Self;

    // method signatures
    // returns a string
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // traits can provide default method definitions
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            println!("{} is already naked...", self.name);
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }    
}

impl Animal for Sheep {
    fn new(name: &'static str) -> Self {
        Sheep { name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // Default trait methods can be overriden
    fn talk(&self) {
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}


fn main() {
    // type annotation is necessary since this is an Animal of type sheep
    let mut dolly: Sheep = Animal::new("Dolly");

    dolly.talk();
    dolly.shear();
    dolly.talk();
}