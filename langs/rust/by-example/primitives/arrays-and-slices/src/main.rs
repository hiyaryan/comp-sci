// Array [T, length]: collection of objects of the 'same' type stored in contiguous memory whose length is known at compile time
// Slices [T]: same as array but whose length is `not` known at compile time

use std::mem;

// borrow a slice 
fn _analyze_slice(slice: &[i32]) {
    println!("first element of the slice: {}", slice[0]);
    println!("the slice has {} elements", slice.len());
}

fn main() {
    // fixed-size array (stating type is redundant)
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // initializing all elements to 0
    let ys: [i32; 500] = [0; 500];

    // indexing starts at 0
    println!("first element of the array: {}", xs[0]);
    println!("second element of the array: {}", xs[1]);

    // return length of array
    println!("length of array: {}", xs.len());

    // arrays are stack allocated
    println!("array occupies {} bytes", mem::size_of_val(&xs));

    // automatically borrow an array as a slice
    _analyze_slice(&xs);

    // point to a section of an array
    println!("borrow a section of the array as a slice");
    _analyze_slice(&ys[1..4]);

    // example of empty slive `&[]`
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // same as above

    // use .get on an array to safely access each element using an Option
    // use .expect to exit the program with a message instead of continuing
    for i in 0..xs.len() + 1 {
        match xs.get(i) {
            Some(xval) => println!("{i}: {xval}"),
            None => println!("Trying to access a element that doesn't exist at index {i}."),
        }
    }

    // Out of bounds runtime error
    // println!("{}", xs[5]);
}
