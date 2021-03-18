from nodeClass import *
class Automata():
    def __init__(self):
        self.node_list=[]
        self.initial_node=None
        self.final_node=None
    def get_initial_node(self):
        return self.initial_node
    
    def get_final_node(self):
        return self.final_node
    
    def get_node_list(self):
        return self.node_list
    
    def set_node_list(self, new_node_list):
        self.node_list = new_node_list

    def set_initial_node(self,new_initial_node):
        self.initial_node=new_initial_node

    def det_final_node(self,new_final_node):
        self.final_node=new_final_node
