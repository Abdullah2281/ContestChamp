# Problem: Projectile Motion

## Introduction

In this problem, you are tasked with calculating the trajectory of a projectile. Projectile motion is a form of motion experienced by an object that is thrown or projected into the air, subject to only the acceleration of gravity. The object is called a projectile, and its path is called its trajectory.

## Problem Statement

A projectile is launched from the ground with an initial velocity \( v_0 \) at an angle \( \theta \) above the horizontal. You need to determine the maximum height reached by the projectile, the total time of flight, and the horizontal range of the projectile.

## Equations

1. **Maximum Height (\( H \)):**

\[ H = \frac{v_0^2 \sin^2(\theta)}{2g} \]

2. **Total Time of Flight (\( T \)):**

\[ T = \frac{2v_0 \sin(\theta)}{g} \]

3. **Horizontal Range (\( R \)):**

\[ R = \frac{v_0^2 \sin(2\theta)}{g} \]

where:
- \( v_0 \) is the initial velocity of the projectile (in meters per second, m/s)
- \( \theta \) is the launch angle (in degrees)
- \( g \) is the acceleration due to gravity (\( 9.81 \, \text{m/s}^2 \))

## Input

The input consists of two space-separated values:
1. \( v_0 \) (1 ≤ \( v_0 \) ≤ 1000) - the initial velocity of the projectile.
2. \( \theta \) (0 < \( \theta \) < 90) - the launch angle in degrees.

## Output

The output should contain three space-separated values:
1. \( H \) - the maximum height reached by the projectile.
2. \( T \) - the total time of flight.
3. \( R \) - the horizontal range.

All outputs should be rounded to two decimal places.

## Example

**Input:**
