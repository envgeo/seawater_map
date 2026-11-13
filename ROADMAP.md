# EnvGeo-Seawater Roadmap

[日本語版](ROADMAP_Japanese.md)

This roadmap describes possible directions after the stable v1.3.5 release. It
is not a schedule or a commitment to implement every item. The public stable
release remains the reference for currently supported functionality.

## Data stewardship and comparison collections

- Assess published Around Japan comparison datasets before inclusion. Any new
  bundled data must have documented provenance, redistribution terms, required
  citation, transformations, and regression tests.
- Continue to distinguish project data, cited external comparison collections,
  and session-only user uploads in the interface and documentation.

## User-data workflows

- Extend upload support to additional visualisation workflows only where the
  required columns, quality checks, provenance labels, and tests are clear.
- Keep browser uploads session-only and visually distinguish uploaded records
  from bundled reference data.

## Maps and deployment reliability

- Monitor Streamlit Community Cloud performance and resource use under normal
  interactive use.
- The public static-map baseline remains the established Plate Carrée
  longitude--latitude view. Reconsider map-projection choices only after a
  separately testable, Cloud-safe design has been demonstrated for repeated
  global Scatter and Contour rendering, extent changes, land/coastline output,
  and downloaded figures in both local and Community Cloud environments.

## Model and proxy comparison

- After a separate safety and performance assessment, consider an optional
  model-grid layer for isotope-enabled
  climate-model output and proxy comparison. Keep grids distinct from point
  observations; begin with subsetted raster or contour backgrounds and retain
  explicit experiment, variable, units, and spatial/temporal matching
  provenance.

## Maintenance and publication

- Prioritise focused bug fixes, documentation corrections, and reproducible
  releases over broad refactoring of the stable application.
- Keep citation records current as datasets and releases evolve.

For detailed internal planning and experimental development, see the separate
development repositories rather than this stable-release roadmap. Detailed
`TODO.md` files are intentionally excluded from the stable repository.
