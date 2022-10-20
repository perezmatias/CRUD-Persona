import unittest
from main import Persona
from main import Personaservice

class TestApp(unittest.TestCase):
    
    def test_add(self):
        repo1=Personaservice()
        persona1=Persona("pepe","honguito",123)
        repo1.add(persona1)
        self.assertDictEqual(repo1.__dict__,{'personas': [persona1] })
        
    def test_delete(self):
        repo1=Personaservice()
        persona1=Persona("Jose","Perez",864)
        repo1.add(persona1)
        repo1.delete(persona1)
        self.assertDictEqual(repo1.__dict__,{'personas': [] })

    def test_update(self):
        repo1=Personaservice()
        persona1=Persona("Juan","Casas",000)
        persona2=Persona("alberto","cortez",85)
        repo1.add(persona1)
        repo1.update(persona1,persona2)
        self.assertDictEqual(repo1.__dict__,{'personas': [persona2] })

    def test_findbydocumento_sucess(self):
        repo1=Personaservice()
        persona1=Persona("Pedro","Razo", 32467)
        repo1.add(persona1)
        self.assertEqual(persona1,repo1.findByDocumento(32467))

    def test_findbydocumento_failed(self):
        repo1=Personaservice()
        persona1=Persona("Pedro","Razo", 32467)
        repo1.add(persona1)
        self.assertEqual(None,repo1.findByDocumento(00000))

    def test_findAll(self):
        repo1=Personaservice()
        persona1=Persona("William","Reyes", 8976)
        persona2=Persona("Don","Juan", 5681)
        repo1.add(persona1)
        repo1.add(persona2)
        self.assertDictEqual(repo1.__dict__,{'personas': [persona1,persona2] })

if __name__ == '__main__':
    unittest.main()