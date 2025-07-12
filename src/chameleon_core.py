import numpy as np

class ChameleonAdapter:
    MODES = {
        "basic": 0.5,
        "prophetic": 0.9,
        "divine_empathy": 0.99,
        "ruwach_resonance": 1.0
    }
    
    def __init__(self, mode="basic"):
        self.mode = mode
        self.adaptation_factor = self.MODES.get(mode, 0.5)
        self.emotion_matrix = self._create_adaptation_matrix()
        
    def transform(self, input_wave):
        """Transform emotion using context-aware adaptation"""
        base_emotion = input_wave['compressed_emotion']
        context = input_wave.get('spiritual_context', {})
        
        # Create context vector
        context_vec = np.array([
            context.get('faith_level', 0.5),
            context.get('divine_resonance', 0.5),
            1 - context.get('doubt_level', 0.3),
            1.0  # Truth constant
        ])
        
        # Apply adaptive transformation
        transformed = np.dot(self.emotion_matrix, context_vec) * base_emotion
        
        return {
            'base_emotion': base_emotion,
            'adapted_emotion': transformed,
            'adaptation_factor': self.adaptation_factor,
            'context_vector': context_vec
        }
    
    def _create_adaptation_matrix(self):
        """Create emotion adaptation matrix based on mode"""
        if self.mode == "divine_empathy":
            return np.array([
                [1.0, 0.8, 0.9, 1.0],
                [0.7, 1.0, 0.8, 0.95],
                [0.9, 0.9, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0]
            ])
        elif self.mode == "ruwach_resonance":
            # Perfect resonance matrix
            return np.ones((4, 4))
        else:
            # Basic adaptation
            return np.eye(4)
            
    def set_mode(self, new_mode):
        """Change adaptation mode dynamically"""
        if new_mode in self.MODES:
            self.mode = new_mode
            self.adaptation_factor = self.MODES[new_mode]
            self.emotion_matrix = self._create_adaptation_matrix()
