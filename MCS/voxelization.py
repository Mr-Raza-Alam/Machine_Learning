"""
Voxelization Utilities for Spatial-Temporal Data
Contains functions for normalizing, scaling, and creating voxel structures
"""

import random


def normalize_coordinates(df):
    """
    Step 1: Normalize coordinates by shifting to origin
    
    Subtracts minimum values so all coordinates start from 0
    
    Args:
        df: DataFrame with 'latitude', 'longitude', 'time_slot' columns
    
    Returns:
        df with new columns 'x', 'y', 't' (normalized coordinates)
        min_values dict with original minimums
    """
    min_values = {
        'latitude': df['latitude'].min(),
        'longitude': df['longitude'].min(),
        'time_slot': df['time_slot'].min()
    }
    
    df['x'] = df['latitude'] - min_values['latitude']
    df['y'] = df['longitude'] - min_values['longitude']
    df['t'] = df['time_slot'] - min_values['time_slot']
    
    return df, min_values


def scale_coordinates(df):
    """
    Step 2: Scale coordinates to make all dimensions comparable
    
    Scales all dimensions to the same range so spatial and temporal
    distances contribute fairly to distance calculations
    
    Args:
        df: DataFrame with normalized 'x', 'y', 't' columns
    
    Returns:
        df with scaled 'x', 'y', 't' columns
        max_values dict with scaling factors used
    """
    max_range = max(df['x'].max(), df['y'].max(), df['t'].max())
    
    max_values = {
        'latitude': df['latitude'].max(),
        'longitude': df['longitude'].max(),
        'time_slot': df['time_slot'].max()
    }
    
    df['x'] = df['x'] / max_values['latitude'] * max_range
    df['y'] = df['y'] / max_values['longitude'] * max_range
    df['t'] = df['t'] / max_values['time_slot'] * max_range
    
    return df, max_values


def create_voxels(df):
    """
    Step 3: Create voxel structure from DataFrame
    
    Converts each row into a voxel dictionary with spatial-temporal
    coordinates and associated value
    
    Args:
        df: DataFrame with 'x', 'y', 't', 'value' columns
    
    Returns:
        List of voxel dictionaries
    """
    voxels = []
    
    for _, row in df.iterrows():
        voxels.append({
            'x': row['x'],
            'y': row['y'],
            't': row['t'],
            'value': row['value'],
            'true_value': row['value']
        })
    
    return voxels


def simulate_data_loss(voxels, loss_probability=0.9):
    """
    Step 4: Simulate missing data by randomly removing values
    
    Args:
        voxels: List of voxel dictionaries
        loss_probability: Probability that each value is lost (0-1)
    
    Returns:
        voxels with some values set to None
        tuple of (known_count, missing_count)
    """
    for v in voxels:
        if random.random() < loss_probability:
            v['value'] = None
    
    known_count = sum(1 for v in voxels if v['value'] is not None)
    missing_count = sum(1 for v in voxels if v['value'] is None)
    
    return voxels, (known_count, missing_count)


def voxelize(df, loss_probability=0.9, simulate_loss=True):
    """
    Complete voxelization pipeline
    
    Performs all steps:
    1. Normalize coordinates (shift to origin)
    2. Scale coordinates (make dimensions comparable)
    3. Create voxel structure
    4. Simulate data loss (optional)
    
    Args:
        df: DataFrame with 'latitude', 'longitude', 'time_slot', 'value' columns
        loss_probability: Probability of data loss (default 0.9)
        simulate_loss: Whether to simulate data loss (default True)
    
    Returns:
        voxels: List of voxel dictionaries
        stats: Dictionary with voxelization statistics
    """
    # Step 1: Normalize
    df, min_values = normalize_coordinates(df)
    
    # Step 2: Scale
    df, max_values = scale_coordinates(df)
    print(df.head(7))    
    # Step 3: Create voxels
    voxels = create_voxels(df)
    
    stats = {
        'total_voxels': len(voxels),
        'min_values': min_values,
        'max_values': max_values
    }
    
    # Step 4: Simulate loss (optional)
    if simulate_loss:
        voxels, (known, missing) = simulate_data_loss(voxels, loss_probability)
        stats['known_count'] = known
        stats['missing_count'] = missing
        stats['loss_probability'] = loss_probability
    
    return voxels, stats
