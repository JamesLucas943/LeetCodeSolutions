class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #----Variable Definitions----
        finalList = ListNode(0)
        tail = finalList
        oneCarry = False

        #----Algorithm----
        while l1 or l2 or oneCarry:
            #gets value from l1
            if l1:
                one = l1.val
                l1 = l1.next
            else:
                one = 0

            #gets value from l2
            if l2:
                two = l2.val
                l2 = l2.next
            else:
                two = 0

            #adds the two values together (taking into account the carry)
            if oneCarry:
                addedValue = one + two + 1
                oneCarry = False
            else:
                addedValue = one + two

            #checking if there is a new carry
            if addedValue > 9:
                addedValue = addedValue - 10
                oneCarry = True

            #assigns the value to the finalList
            tail.next = ListNode(addedValue)
            tail = tail.next

        return finalList.next
