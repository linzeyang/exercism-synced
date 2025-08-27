pub fn is_armstrong_number(num: u32) -> bool {
    let num_str = num.to_string();
    let num_len = num_str.len();
    let sum: u32 = num_str.chars()
        .map(|c| c.to_digit(10).unwrap()) // Convert char to u32
        .map(|d| d.pow(num_len as u32))   // Raise to the power of the number of digits
        .sum();                          // Sum all the powered digits

    sum == num
}
