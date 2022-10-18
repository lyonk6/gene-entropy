
class AssembleRibozyme:
    def __init__(self, initial_sequence):
        self.sequence = initial_sequence
    
    def append_residue(self):
        return

    def append_subset(self):
        return
    
    def is_done(self, target):
        if self.sequence == target:
            return True
        else:
            return False


if __name__ == '__main__':
    # The find() method returns the position of the first occurrence
    # of a specified value and returns -1 if the value is not found.
    #pos   0123456789
    rna = 'gguucaugug'

    pos = rna.find('gug')
    print(pos)
    
    print("Where is it? ", pos)

