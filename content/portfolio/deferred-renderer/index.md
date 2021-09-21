---
title: Deferred Renderer
description: Deferred renderer
date: "2020-04-21T00:00:00+00:00"
jobDate: 2020
work: [Graphics, School]
techs: [C++, OpenGL]
thumbnail: deferred-renderer/green-bloom.png
---

![Project gif](/portfolio/deferred-renderer/bloom.gif)

The final project in my computer graphics was to implement dynamic geometry, deferred rendering, and bloom in OpenGL.
I went on to extend this project with tiled-deferred rendering as well.

### Dynamic Geometry
There are various geometrical objects with transformations in this project, including: bouncing spheres, surfaces of revolution that deform, rotating bunnies, and shearing teapots.

### Deferred Rendering
Instead of having one rendering pass whereby the scene is rendered directly to the screen, in deferred rendering we have two passes. 
In the first pass we render the normal, diffuse, position, and emissive lighting attributes to their own textures.
For the secon pass we draw a fullscreen quad and apply these textures with the lighting component onto the quad.

### Bloom
Bloom is a post-processing method that gives light sources a glow effect.
I used a Gaussian-Filter implementation for my bloom.
The bloom effect is it's own texture which is computed after the first render pass but before the second.

### Tiled-Deferred Rendering
Tiled-deferred rendering becomes necessary when there are a lot of lights in a scene. It increases performance by only applying light sources to a fragment if they effect it.
The first step in this process is dividing the view frustum into several different frustums, where each frustum corresponds to a different tile in the near plane.
In the second pass we loop through each of these view frustums and perform a view-frustum intersection test on each light. 
If the light's area of effect (governed by its attenuation) is inside or intersecting the frustum, we include that light in that tile's fragment computation.