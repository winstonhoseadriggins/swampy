import sys

message = """
If you can read this, you are all set for the final.

A few bits of advice:

1) If you have any doubts about the reliability of wireless, bring
   a network cable to the exam.

2) On the day of the exam, I will add a file to this directory.

3) When you get to the exam (but not before), you will update your
   repository to get the file.

4) When you are done with the exam, you will check in your repository
   to upload the changes you made.

5) I will bring a laptop to the exam so I can confirm that your
   changes were uploaded before you leave.

6) If anything goes wrong, with the mechanics of this process, don't
   let it distract you from the exam.  Focus on the exam -- we can
   work out the hitches later.

7) If you get stuck on a programming question, don't spend too much
   time debugging.  If you think your answer is close to correct,
   leave it at that and move on to the next problem.  If you have
   time, you can come back to it.

See you next week.  Good luck!

Allen


"""


def main(script, *args):
    print script, args
    print message

if __name__ == '__main__':
    main(*sys.argv)
