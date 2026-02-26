"""
Visualization Utilities for 3D Voxel Data
Contains functions for plotting spatial-temporal data and prediction analysis
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot_3d_voxels(voxels, title, color_by='value', show_missing=False):
    """
    Plot 3D scatter of voxels with color-coded values
    
    Args:
        voxels: List of voxel dictionaries
        title: Plot title
        color_by: Which value to use for coloring ('value' or 'true_value')
        show_missing: If True, show known vs missing points with different markers
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    if show_missing:
        # Separate known and missing points
        known = [v for v in voxels if v['value'] is not None]
        missing = [v for v in voxels if v['value'] is None]
        
        # Plot known values (colored by value)
        if known:
            x_k = [v['x'] for v in known]
            y_k = [v['y'] for v in known]
            t_k = [v['t'] for v in known]
            val_k = [v['value'] for v in known]
            sc1 = ax.scatter(x_k, y_k, t_k, c=val_k, cmap='viridis', s=100, 
                           marker='o', label=f'Known ({len(known)})', alpha=0.9)
            plt.colorbar(sc1, ax=ax, label='Value', shrink=0.6)
        
        # Plot missing values (red X)
        if missing:
            x_m = [v['x'] for v in missing]
            y_m = [v['y'] for v in missing]
            t_m = [v['t'] for v in missing]
            ax.scatter(x_m, y_m, t_m, c='red', s=80, marker='x', 
                      label=f'Missing ({len(missing)})', alpha=0.7)
        ax.legend()
    else:
        # Plot all points with color by value
        x = [v['x'] for v in voxels]
        y = [v['y'] for v in voxels]
        t = [v['t'] for v in voxels]
        values = [v[color_by] for v in voxels]
        
        scatter = ax.scatter(x, y, t, c=values, cmap='viridis', s=100, alpha=0.8)
        plt.colorbar(scatter, ax=ax, label='Value', shrink=0.6)
    
    ax.set_xlabel('X (Latitude)')
    ax.set_ylabel('Y (Longitude)')
    ax.set_zlabel('T (Time)')
    ax.set_title(title)
    plt.tight_layout()
    plt.show()


def plot_predicted_vs_actual(voxels, normalized_error):
    """
    Plot side-by-side 3D comparison of predicted vs actual values
    
    Args:
        voxels: List of voxel dictionaries (must have 'predicted' key for missing ones)
        normalized_error: The calculated normalized error percentage
    """
    predicted_voxels = [v for v in voxels if 'predicted' in v]
    
    if not predicted_voxels:
        print("No predicted voxels to display!")
        return
    
    fig = plt.figure(figsize=(14, 6))
    
    # Extract coordinates
    x_p = [v['x'] for v in predicted_voxels]
    y_p = [v['y'] for v in predicted_voxels]
    t_p = [v['t'] for v in predicted_voxels]
    
    # Subplot 1: Predicted values
    ax1 = fig.add_subplot(121, projection='3d')
    pred_vals = [v['predicted'] for v in predicted_voxels]
    sc1 = ax1.scatter(x_p, y_p, t_p, c=pred_vals, cmap='plasma', s=100, marker='^')
    plt.colorbar(sc1, ax=ax1, label='Predicted Value', shrink=0.6)
    ax1.set_xlabel('X (Latitude)')
    ax1.set_ylabel('Y (Longitude)')
    ax1.set_zlabel('T (Time)')
    ax1.set_title('Predicted Values (Missing Points)')
    
    # Subplot 2: Actual (True) values
    ax2 = fig.add_subplot(122, projection='3d')
    actual_vals = [v['true_value'] for v in predicted_voxels]
    sc2 = ax2.scatter(x_p, y_p, t_p, c=actual_vals, cmap='plasma', s=100, marker='o')
    plt.colorbar(sc2, ax=ax2, label='Actual Value', shrink=0.6)
    ax2.set_xlabel('X (Latitude)')
    ax2.set_ylabel('Y (Longitude)')
    ax2.set_zlabel('T (Time)')
    ax2.set_title('Actual Values (Ground Truth)')
    
    plt.suptitle(f'Predicted vs Actual (Normalized Error: {normalized_error*100:.2f}%)', fontsize=14)
    plt.tight_layout()
    plt.show()


def plot_error_analysis(voxels):
    """
    Plot error distribution histogram and predicted vs actual scatter
    
    Args:
        voxels: List of voxel dictionaries with predictions
    """
    predicted_voxels = [v for v in voxels if 'predicted' in v]
    
    if not predicted_voxels:
        print("No predicted voxels to analyze!")
        return
    
    errors = [abs(v['true_value'] - v['predicted']) for v in predicted_voxels]
    pred_list = [v['predicted'] for v in predicted_voxels]
    actual_list = [v['true_value'] for v in predicted_voxels]
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram of errors
    axes[0].hist(errors, bins=15, color='steelblue', edgecolor='black', alpha=0.7)
    axes[0].axvline(np.mean(errors), color='red', linestyle='--', 
                    label=f'Mean Error: {np.mean(errors):.2f}')
    axes[0].set_xlabel('Absolute Error')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Error Distribution')
    axes[0].legend()
    
    # Predicted vs Actual scatter
    axes[1].scatter(actual_list, pred_list, c='steelblue', alpha=0.7, s=50)
    
    # Perfect prediction line
    min_val = min(min(actual_list), min(pred_list))
    max_val = max(max(actual_list), max(pred_list))
    axes[1].plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect Prediction')
    axes[1].set_xlabel('Actual Value')
    axes[1].set_ylabel('Predicted Value')
    axes[1].set_title('Predicted vs Actual')
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()
