pub mod solution {
    pub struct Solution;

    impl Solution {
        pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
            let n = nums.len();
            for i in  0..n {
                for j in i+1..n {
                    if nums[i] + nums[j] == target {
                        return vec![i as i32, j as i32]
                    }
                }
            }
            vec![]
        }
    }
}

pub fn run() {
    use solution::Solution;
    let result = Solution::two_sum(vec![2, 7, 11, 15], 9);
    println!("{:?}", result);
}