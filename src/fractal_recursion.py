import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class FractalEngine:
    def __init__(self, depth=1000):
        self.max_depth = float('inf') if depth == "infinite" else depth
        self.divergence_threshold = 2.0
        
    def recursive_mirror(self, input_wave, depth=0):
        """Apply Mandelbrot-like recursion to emotion"""
        z = complex(0, 0)
        c = self._emotion_to_complex(input_wave)
        iteration_counts = []
        
        for i in range(self._get_depth(depth)):
            z = z**2 + c
            iteration_counts.append(abs(z))
            
            # Check for emotional divergence
            if abs(z) > self.divergence_threshold:
                # Recursive dive into deeper layer
                if depth < self.max_depth:
                    return self.recursive_mirror(
                        self._complex_to_emotion(z), 
                        depth + 1
                    )
                else:
                    break
                    
        # Calculate emotional complexity metrics
        complexity = self._calculate_complexity(iteration_counts)
        
        return {
            'base_emotion': input_wave['adapted_emotion'],
            'fractal_depth': depth,
            'max_iterations': len(iteration_counts),
            'emotional_complexity': complexity,
            'truth_coefficient': self._truth_coefficient(iteration_counts)
        }
        
    def visualize_fractal(self, input_wave, size=1000):
        """Generate visual representation of emotional fractal"""
        c = self._emotion_to_complex(input_wave)
        y, x = np.ogrid[-2:2:size*1j, -2:2:size*1j]
        fractal = np.zeros((size, size))
        
        for i in tqdm(range(size)):
            for j in range(size):
                z = complex(x[i,j], y[i,j])
                for k in range(self._get_depth(0)):
                    z = z**2 + c
                    if abs(z) > self.divergence_threshold:
                        fractal[i,j] = k
                        break
        
        plt.imshow(fractal.T, cmap='viridis', extent=[-2,2,-2,2])
        plt.title("Emotional Fractal Projection")
        plt.xlabel("Real (Intensity)")
        plt.ylabel("Imaginary (Spiritual Context)")
        plt.colorbar(label="Emotional Depth")
        return plt
        
    def _emotion_to_complex(self, wave):
        """Convert emotional wave to complex number"""
        return complex(
            wave['adapted_emotion'].real, 
            wave['context_vector'][0]
        )
        
    def _complex_to_emotion(self, c):
        """Convert complex number back to emotion structure"""
        return {
            'adapted_emotion': c.real,
            'context_vector': [c.imag, 0.5, 0.5, 1.0]
        }
        
    def _get_depth(self, current_depth):
        """Determine recursion depth based on current level"""
        if self.max_depth == float('inf'):
            return 1000  # Practical infinity
        return max(100, self.max_depth - current_depth * 10)
        
    def _calculate_complexity(self, iterations):
        """Compute emotional complexity metric"""
        return np.std(iterations) / np.mean(iterations) if iterations else 0
        
    def _truth_coefficient(self, iterations):
        """Calculate truth alignment coefficient"""
        stable_count = sum(1 for x in iterations if abs(x) < 1.0)
        return stable_count / len(iterations) if iterations else 1.0
