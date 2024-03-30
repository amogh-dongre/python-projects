#!/usr/bin/env python3
class Slice:
    s : str
    start : int
    end : int
    def rec_str(self,s : str, start : int, end : int) :
        if (start == (end-1)):
            print("\n Done")
        else :
            print(s[start+1])
            rec_str(self,s,start+1,end)
    def SetS(self):
        s = input("Enter the string: ")
    def SetStart(self):
        start = int(input("Enter the first index : "))
    def Setend(self):
        end = int(input("Enter the last index :  "))
class assignment:
    def main(self):
        s1 = Slice()
        s1.SetS()
        s1.SetStart()
        s1.Setend()
        s1.rec_str(s1.s,s1.start,s1.end)
if __name__ == "__main__":
    test_assignment = assignment()
    test_assignment.main()
