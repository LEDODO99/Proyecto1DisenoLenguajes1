class Node():
    def __init__(self):
        self.node_name=""
        self.node_transitions=[]

    def create_transition(self,symbol,objective):
        self.node_transitions.append([symbol,objective])
    def define_name(self,new_name):
        self.node_name = new_name
    def get_node_name(self):
        return self.node_name
    def get_node_transitions(self):
        return self.node_transitions
    
