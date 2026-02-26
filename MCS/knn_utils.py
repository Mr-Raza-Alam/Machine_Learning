"""
KNN Utilities for Spatial-Temporal Data Imputation
Contains distance functions and KNN prediction algorithm using Inverse Distance Weighting
"""

import math
import numpy as np


def spatial_dist(a, b):
    """Calculate Euclidean distance between two points in 2D space (x, y)"""
    return math.sqrt((a['x'] - b['x'])**2 + (a['y'] - b['y'])**2)


def temporal_dist(a, b):
    """Calculate absolute temporal distance between two points"""
    return abs(a['t'] - b['t'])


def spatio_temporal_dist(a, b, alpha):
    """
    Calculate combined spatio-temporal distance
    
    Args:
        a, b: Voxel dictionaries with 'x', 'y', 't' keys
        alpha: Weight for spatial vs temporal (0-1)
               Higher alpha = more weight to spatial distance
    
    Returns:
        Weighted combination of spatial and temporal distance
    """
    return alpha * spatial_dist(a, b) + (1 - alpha) * temporal_dist(a, b)


def knn_predict(target, voxels, k, alpha=0.5, mode='ST', prediction_type='weighted'):
    """
    Predict missing value using K-Nearest Neighbors with Inverse Distance Weighting
    
    Weighted KNN Formula (Inverse Distance Weighting):
    predicted_value = Σ(value_i / distance_i) / Σ(1 / distance_i)
    Closer neighbors have higher weights (1/d is larger when d is smaller)
    
    Args:
        target: Voxel with missing value to predict
        voxels: List of all voxels
        k: Number of nearest neighbors to use
        alpha: Spatio-temporal distance weight (default 0.5)
        mode: Distance mode - 'ST' for spatio-temporal
        prediction_type: 'naive' (simple average) or 'weighted' (IDW)
    
    Returns:
        Predicted value for the target voxel
    """
    distances = []
    
    for v in voxels:
        # Skip the target itself and voxels with missing values
        if v is not target and v['value'] is not None:
            d = spatio_temporal_dist(target, v, alpha)
            distances.append((d, v['value']))
    
    # Sort and get k nearest neighbors
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]
    
    if not neighbors:
        return None
    
    if prediction_type == 'naive':
        # Simple average
        return np.mean([val for _, val in neighbors])
    
    elif prediction_type == 'weighted':
        # Inverse Distance Weighting
        sumd = 0
        for d, val in neighbors:
            sumd += (1.0 / d) if d != 0 else 1e-9
        
        xd = 0
        for d, val in neighbors:
            weight = (1.0 / d) if d != 0 else 1e-9
            xd += (weight / sumd) * val
        
        return xd  # This is the predicted value
    
    return None
