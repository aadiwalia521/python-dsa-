scores = [65, 90, 45, 82, 71]
pass_count = 0

for s in scores:
  if s >=70:
    pass_count = pass_count+1
    print(f"the total number of students is:  {s}")
  else:
    print(f"they students who did not passed are : {s}")
