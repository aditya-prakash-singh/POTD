#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    while head1 and head2 and head1.data==head2.data :
        head1=head1.next
        head2=head2.next
    return True if head1==head2 else False