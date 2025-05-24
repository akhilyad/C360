import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from emissions import calculate_distance, calculate_co2, optimize_route

def test_calculate_distance():
    # Example: London to Paris (should be >0)
    dist = calculate_distance('United Kingdom', 'London', 'France', 'Paris')
    assert dist > 0

def test_calculate_co2():
    # Example: 1000 km, 10 tons, Truck
    co2 = calculate_co2('Truck', 1000, 10)
    assert co2 > 0

def test_optimize_route():
    # Example: London to Paris, 1000 km, 10 tons
    best_option, min_co2, breakdown, distances, current_co2 = optimize_route(
        'United Kingdom', 'London', 'France', 'Paris', 1000, 10, prioritize_green=True
    )
    assert min_co2 < current_co2 