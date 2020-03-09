<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.0" minimumScale="inf" maximumScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <pipe>
    <rasterrenderer opacity="1" alphaBand="0" classificationMax="0.015" classificationMinMaxOrigin="User" band="1" classificationMin="-0.015" type="singlebandpseudocolor">
      <rasterTransparency/>
      <rastershader>
        <colorrampshader colorRampType="DISCRETE" clip="0">
          <item alpha="255" value="-0.01" label="&lt;= -0.01" color="#ff0000"/>
          <item alpha="255" value="-0.005" label="-0.01 - -0.005" color="#ff6666"/>
          <item alpha="255" value="0" label="-0.005 - 0" color="#ffcccc"/>
          <item alpha="255" value="0.005" label="0 - 0.005" color="#ccccff"/>
          <item alpha="255" value="0.01" label="0.005 - 0.01" color="#6666ff"/>
          <item alpha="255" value="inf" label="> 0.01" color="#0000ff"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
