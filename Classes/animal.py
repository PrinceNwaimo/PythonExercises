class Animal:

    def __init__(self, name, speak, dance):
        self.animal_name = name
        self.animal_speech = speak
        self.animal_dance_skill = dance


    def set_animal_name(self, name):#setter method
        self.animal_name = name

    def get_animal_name(self):#getter method
        return self.animal_name

    def set_animal_speech(self,speak):
        self.animal_speech = speak

    def get_animal_speech(self):
        return self.animal_speech

    def set_animal_dance_skill(self,dance):
        self.animal_dance_skill = dance

    def get_animal_dance_skill(self):
        return self.animal_dance_skill

    def set_animal_run(self,race):
        self.animal_run = race

    def get_animal_run(self):
        return self.animal_run

    def set_animal_list(self,*values):
        # for i in range (len(values)):
        #     self.animal_list.append(values[i])
            # self.animal_list_size += 1
        self.animal_list= [i for i in values]
    def get_animal_list(self):
        return self.animal_list

    def get_animal_list_size(self):
        return len(self.animal_list)
