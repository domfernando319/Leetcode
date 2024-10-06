if len(nums) < 2:
        return 0

    min_value = min(nums)
    max_value = max(nums)

    # Calculate the size of each bucket
    bucket_size = max(1, (max_value - min_value) // (len(nums) - 1))
    bucket_count = (max_value - min_value) // bucket_size + 1

    # Create buckets
    buckets = [[None, None] for _ in range(bucket_count)]

    # Place numbers into buckets
    for num in nums:
        bucket_index = (num - min_value) // bucket_size
        if buckets[bucket_index][0] is None:  # If this is the first number in the bucket
            buckets[bucket_index][0] = num  # Min
            buckets[bucket_index][1] = num  # Max
        else:
            buckets[bucket_index][0] = min(buckets[bucket_index][0], num)  # Update Min
            buckets[bucket_index][1] = max(buckets[bucket_index][1], num)  # Update Max

    # Calculate the maximum gap
    max_gap = 0
    previous_max = min_value

    for bucket in buckets:
        if bucket[0] is None:  # Empty bucket
            continue
        # The gap is the difference between the min of the current bucket and the max of the previous bucket
        max_gap = max(max_gap, bucket[0] - previous_max)
        previous_max = bucket[1]

    return max_gap