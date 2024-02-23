use std::fmt::{Display, Formatter, Result};

#[derive(Debug)]
struct Matrix(f32, f32, f32, f32); // A tuple struct.

impl Display for Matrix {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(f, "({} {})\n({} {})", self.0, self.1, self.2, self.3)
    }
}

// Accepts a tuple argument and returns a tuple
fn _reverse(pair: (i32, bool)) -> (bool, i32) {
    // bind members of a tuple into variables
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

fn _transpose(matrix: Matrix) -> Matrix {
    Matrix(matrix.0, matrix.2, matrix.1, matrix.3)
}

// Tuple (T1, T2, ...): a collection of values of different types
fn main() {
    // a tuple of all types
    let _long_tuple = (1u8, 2u16, 3u32, 4u64, -1i8, -2i16, -3i32, -4i64, 0.1f32, 0.2f64, 'a', true);

    // Extract values from the tuples using "tuple indexing"
    println!("long tuple first value {}", _long_tuple.0);
    println!("long tuple second value {}", _long_tuple.1);

    // tuple made of tuples
    let _tuples_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // print tuples
    println!("tuple of tuples {_tuples_of_tuples:?}");

    // note that tuples greater than 12 elements cannot be printed
    let _too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    // println!("can't print tuple this long {:?}", _too_long_tuple); // Error: `Debug` is not implemented
    let _almost_too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
    println!("tuple is almost too long to print {_almost_too_long_tuple:?}");

    // passing a tuple as an argument
    let pair = (1, true);
    println!("pair is {pair:?}");
    println!("the reversed pair is {:?}", _reverse(pair));

    // a tuple of 1 needs a comma to distinguish it from a literal value surrounded by parenthesis
    println!("one element tuple: {:?}", (5u32,));
    println!("just an integer: {:?}", (5u32));

    // tuples can be destructured to create bindings
    let tuple = (1, "hello", 4.5, true);
    
    let (a, b, c, d) = tuple;
    println!("printing all tuple members from destructured variables {a:?}, {b:?}, {c:?}, {d:?}");

    // using a tuple matrix
    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("Matrix: \n{matrix}");

    println!("Transpose: \n{}", _transpose(matrix));
}