import unittest
from animal import Animal


class TestAnimalClass(unittest.TestCase):
    animal = Animal("snopy", "Igbo", "100 mile")

    def test_animal_color(self):
        # given
        self.animal.set_animal_name("snopy")
        # when
        result = self.animal.get_animal_name()
        # assert
        self.assertEquals("snopy", result)

    def test_animal_speech(self):
        self.animal.set_animal_speech("speak")
        result = self.animal.get_animal_speech()
        self.assertEquals("speak", result)

    def test_animal_run(self):
        self.animal.set_animal_run("100 mile")
        result = self.animal.get_animal_run()
        self.assertTrue("100 mile",result)

    def test_animal_list(self):
        self.animal.set_animal_list("Lion",23,"tiger",["puma","lynx"],67)
        count = self.animal.get_animal_list_size()
        self.assertEquals(5,count)
        print()