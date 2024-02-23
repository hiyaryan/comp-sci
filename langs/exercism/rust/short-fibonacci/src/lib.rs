/// Create an empty vector
pub fn create_empty() -> Vec<u8> {
    Vec::<u8>::new()
}

/// Create a buffer of `count` zeroes.
///
/// Applications often use buffers when serializing data to send over the network.
pub fn create_buffer(count: usize) -> Vec<u8> {
    vec![0; count]
}

/// Create a vector containing the first five elements of the Fibonacci sequence.
///
/// Fibonacci's sequence is the list of numbers where the next number is a sum of the previous two.
/// Its first five elements are `1, 1, 2, 3, 5`.
pub fn fibonacci() -> Vec<u8> {
    let mut v = vec![1, 1];
    
    while v.len() < 5 {
        v.push(v[v.len()-2] + v[v.len()-1]);
    }

    v
}
