pub fn square_of_sum(n: u32) -> u32 {
    let sum: u32 = (1 + n) * n / 2;

    sum * sum
}

pub fn sum_of_squares(n: u32) -> u32 {
    let mut sum: u32 = 0;

    for i in 1..n+1 {
        sum += i * i;
    }

    sum
}

pub fn difference(n: u32) -> u32 {
    square_of_sum(n) - sum_of_squares(n)
}
