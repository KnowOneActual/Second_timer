import time

def countdown(seconds):
  """Counts down from the given number of seconds.

  Args:
    seconds: The number of seconds to count down from.
  """

  while seconds > 0:
    print(f"Countdown: {seconds} seconds")
    time.sleep(1)
    seconds -= 1

  print("Times up!")

if __name__ == "__main__":
  seconds = int(input("How many seconds do you want to count down from? "))
  countdown(seconds)