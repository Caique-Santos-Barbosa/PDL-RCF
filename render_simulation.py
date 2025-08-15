"""
Módulo de simulação para Render quando face_recognition não está disponível
"""
import random
import time
from datetime import datetime

class SimulationFacialRecognition:
    """Simula reconhecimento facial para demonstração no Render"""
    
    def __init__(self):
        self.known_users = [
            "Caique Santos",
            "Administrador",
            "Usuário Demo",
            "Visitante"
        ]
        self.last_recognition = {}
        self.recognition_cooldown = 3  # segundos
        
    def simulate_recognition(self, image_data=None):
        """Simula reconhecimento facial"""
        current_time = time.time()
        
        # Verificar cooldown para evitar spam
        if current_time - self.last_recognition.get('time', 0) < self.recognition_cooldown:
            return {'status': 'cooldown', 'message': 'Aguarde alguns segundos'}
        
        # Simular processamento
        time.sleep(0.5)
        
        # 70% de chance de reconhecimento bem-sucedido
        if random.random() < 0.7:
            user = random.choice(self.known_users)
            self.last_recognition = {'time': current_time, 'user': user}
            
            return {
                'status': 'success',
                'name': user,
                'simulation': True,
                'confidence': random.uniform(0.8, 0.95)
            }
        else:
            return {'status': 'fail', 'message': 'Rosto não reconhecido'}
    
    def get_known_faces(self):
        """Retorna lista de rostos conhecidos simulados"""
        return self.known_users
    
    def add_known_face(self, name, image_data=None):
        """Simula adição de rosto conhecido"""
        if name not in self.known_users:
            self.known_users.append(name)
        return {'status': 'success', 'message': f'Rosto de {name} adicionado'}

# Instância global para simulação
simulation_system = SimulationFacialRecognition()

def simulate_face_recognition(image_data):
    """Função global para simular reconhecimento facial"""
    return simulation_system.simulate_recognition(image_data)

def get_simulation_users():
    """Retorna usuários simulados"""
    return simulation_system.get_known_faces()

def add_simulation_user(name):
    """Adiciona usuário simulado"""
    return simulation_system.add_known_face(name) 