#[derive(Debug, PartialEq, Eq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    if *_first_list == *_second_list {
        Comparison::Equal

    } else if _first_list.len() < _second_list.len() {
        // If the first has all the same values as second in the same order but is smaller 
        // then it is a sublist of second. 
        
        // TODO: Deal with the situation where the values are not in the same order.
        // Assume that because the problem did not state the lists are sorted that they are unsorted.
        // Assume that because the problem did not state the lists are only integers that they can hold any type.

        for mut i in 0.._second_list.len() {
            for j in 0.._first_list.len() {
                // do these two elements match?
                // if they do, do the next elements match?
                // If we reaach the end of first list in this loop with all of the results matching, then return is sublist
                // If there are no matches then break and start i from j, so from = j
                if _first_list[j] != _second_list[i] {
                    i += j;
                } else {
                    i += 1;

                    if j == _first_list.len() - 1 {
                        return Comparison::Sublist;
                    }
                }
            }
        }

        Comparison::Unequal

    } else  {
        // If the first has all the same values as second in the same order but second is smaller 
        // then first is a superlist of second.

        // TODO: Deal with the situation where the values are not in the same order.

        for mut i in 0.._first_list.len() {
            for j in 0.._second_list.len() {
                // do these two elements match?
                // if they do, do the next elements match?
                // If we reaach the end of first list in this loop with all of the results matching, then return is sublist
                // If there are no matches then break and start i from j, so from = j
                if _second_list[j] != _first_list[i] {
                    i += j;
                } else {
                    i += 1;

                    if j == _second_list.len() - 1 {
                        return Comparison::Superlist;
                    }
                }
            }
        }


        Comparison::Unequal

    } 
}
