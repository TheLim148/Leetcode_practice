#[allow(dead_code)]
pub mod solution {
    pub struct Solution;

    impl Solution {
        pub fn is_palindrome(x: i32) -> bool {
            if x.to_string() == x.to_string().chars().rev().collect::<String>() {
                return true
            }
            return false
        }
    }
}

#[allow(dead_code)]
pub fn run() {
    use solution::Solution;
    let result = Solution::is_palindrome(-121);
    println!("{:?}", result);
}