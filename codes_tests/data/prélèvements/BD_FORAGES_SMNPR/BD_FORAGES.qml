<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.20" simplifyAlgorithm="0" minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="0" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" readOnly="0" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
  <edittypes>
    <edittype widgetv2type="TextEdit" name="NUM_OUVR">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="NOM_OUVR">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="TYPE_OUVR">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="DRAIN" value="DRAIN"/>
        <value key="FORAGE" value="FORAGE"/>
        <value key="PIEZOMETRE" value="PIEZOMETRE"/>
        <value key="PUITS" value="PUITS"/>
        <value key="PUITS-FORÉ" value="PUITS-FORE"/>
        <value key="SONDAGE" value="SONDAGE"/>
        <value key="SOURCE" value="SOURCE"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="PROF_M">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="PROF_MESUR">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="NAPPE">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="INDTERMINE" value="INDETERMINE"/>
        <value key="KARST CORBIERES" value="KARST DEVONIEN"/>
        <value key="PLIOCENE" value="PLIOCENE"/>
        <value key="QUATERNAIRE" value="QUATERNAIRE"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="ValueMap" name="NAT_TUBAGE">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="Acier" value="ACIER"/>
        <value key="Brique" value="BRIQUE"/>
        <value key="Buse béton" value="BUSE BETON"/>
        <value key="Béton" value="BETON"/>
        <value key="Inox" value="INOX"/>
        <value key="Maconné" value="MAÇONNÉ"/>
        <value key="PVC" value="PVC"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="DIAM_MM">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="CheckBox" name="COUPE_GEOL">
      <widgetv2config fieldEditable="1" UncheckedState="FAUX" constraint="" CheckedState="VRAI" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="CheckBox" name="COUPE_TECH">
      <widgetv2config fieldEditable="1" UncheckedState="FAUX" constraint="" CheckedState="VRAI" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="USAGES">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="AEP COLLECTIF" value="AEP COLLECTIF"/>
        <value key="AEP INDUSTRIEL" value="AEP INDUSTRIEL"/>
        <value key="AEP PRIVE" value="AEP PRIVE"/>
        <value key="AEP+IRRIGATION" value="AEP+IRRIGATION"/>
        <value key="CAMPING" value="CAMPING"/>
        <value key="CHEPTEL" value="CHEPTEL"/>
        <value key="CHEPTEL+IRRIGATION" value="CHEPTEL+IRRIGATION"/>
        <value key="COLLECTIF" value="COLLECTIF"/>
        <value key="DEFENSE INCENDIE" value="DEFENSE INCENDIE"/>
        <value key="DOMESTIQUE" value="DOMESTIQUE"/>
        <value key="GEOTHERMIE" value="GEOTHERMIE"/>
        <value key="INDUSTRIEL" value="INDUSTRIEL"/>
        <value key="IRRIGATION" value="IRRIGATION"/>
        <value key="IRRIGATION+PISCINE" value="IRRIGATION+PISCINE"/>
        <value key="LAVAGE" value="LAVAGE"/>
        <value key="PIEZOMETRE" value="PIEZOMETRE"/>
        <value key="PISCICULTURE" value="PISCICULTURE"/>
        <value key="PISCINE" value="PISCINE"/>
        <value key="SONDAGE" value="SONDAGE"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="ValueMap" name="ETAT">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="" value="{2839923C-8B7D-419E-B84B-CA2FE9B80EC7}"/>
        <value key="ABANDONNÉ" value="ABANDONNÉ"/>
        <value key="EXPLOITÉ" value="EXPLOITÉ"/>
        <value key="REBOUCHÉ" value="REBOUCHÉ"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="DateTime" name="DATE_OUVR">
      <widgetv2config fieldEditable="1" calendar_popup="0" allow_null="1" display_format="dd/MM/yyyy" field_format="yyyy-MM-dd" constraint="" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="X_L93">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="Y_L93">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="LONG_WGS84">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="LAT_WGS84">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="Z_M">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="QUALIT_LOC">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="BONNE (&lt;50m)" value="BONNE (&lt;50m)"/>
        <value key="MAUVAISE (>500m)" value="MAUVAISE (>500m)"/>
        <value key="MOYENNE (50 à 500m)" value="MOYENNE (50 à 500m)"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="CheckBox" name="CORREC_LOC">
      <widgetv2config fieldEditable="1" UncheckedState="FAUX" constraint="" CheckedState="VRAI" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="Z_PRECIS">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="" value="{2839923C-8B7D-419E-B84B-CA2FE9B80EC7}"/>
        <value key="+/- 10cm" value="C10"/>
        <value key="+/- 10m" value="M10"/>
        <value key="+/- 1m" value="M01"/>
        <value key="+/- 50cm" value="C50"/>
        <value key="+/- 50m" value="M50"/>
        <value key="+/- 5m" value="M05"/>
        <value key="EPD - Cote estimé d'après plan directeur" value="EPD"/>
        <value key="Modele Num Terrain" value="MNT"/>
        <value key="Rattachement NGF" value="RNG"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="ValueMap" name="COMMUNE">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="ALENYA" value="ALENYA"/>
        <value key="ARGELES-SUR-MER" value="ARGELES-SUR-MER"/>
        <value key="BAGES" value="BAGES"/>
        <value key="BAHO" value="BAHO"/>
        <value key="BAIXAS" value="BAIXAS"/>
        <value key="BANYULS-DELS-ASPRES" value="BANYULS-DELS-ASPRES"/>
        <value key="BOMPAS" value="BOMPAS"/>
        <value key="BOULETERNERE" value="BOULETERNERE"/>
        <value key="BROUILLA" value="BROUILLA"/>
        <value key="CABESTANY" value="CABESTANY"/>
        <value key="CALCE" value="CALCE"/>
        <value key="CAMELAS" value="CAMELAS"/>
        <value key="CANET-EN-ROUSSILLON" value="CANET-EN-ROUSSILLON"/>
        <value key="CANOHES" value="CANOHES"/>
        <value key="CASTELNOU" value="CASTELNOU"/>
        <value key="CERET" value="CERET"/>
        <value key="CLAIRA" value="CLAIRA"/>
        <value key="CORBERE" value="CORBERE"/>
        <value key="CORBERE-LES-CABANES" value="CORBERE-LES-CABANES"/>
        <value key="CORNEILLA-DEL-VERCOL" value="CORNEILLA-DEL-VERCOL"/>
        <value key="CORNEILLA-LA-RIVIERE" value="CORNEILLA-LA-RIVIERE"/>
        <value key="ELNE" value="ELNE"/>
        <value key="ESPIRA-DE-L-AGLY" value="ESPIRA-DE-L-AGLY"/>
        <value key="FOURQUES" value="FOURQUES"/>
        <value key="ILLE-SUR-TET" value="ILLE-SUR-TET"/>
        <value key="LAROQUE-DES-ALBERES" value="LAROQUE-DES-ALBERES"/>
        <value key="LATOUR-BAS-ELNE" value="LATOUR-BAS-ELNE"/>
        <value key="LE BARCARES" value="LE BARCARES"/>
        <value key="LE BOULOU" value="LE BOULOU"/>
        <value key="LE SOLER" value="LE SOLER"/>
        <value key="LEUCATE" value="LEUCATE"/>
        <value key="LLUPIA" value="LLUPIA"/>
        <value key="MAUREILLAS-LAS-ILLAS" value="MAUREILLAS-LAS-ILLAS"/>
        <value key="MILLAS" value="MILLAS"/>
        <value key="MONTAURIOL" value="MONTAURIOL"/>
        <value key="MONTESCOT" value="MONTESCOT"/>
        <value key="MONTESQUIEU-DES-ALBERES" value="MONTESQUIEU-DES-ALBERES"/>
        <value key="NEFIACH" value="NEFIACH"/>
        <value key="ORTAFFA" value="ORTAFFA"/>
        <value key="PALAU-DEL-VIDRE" value="PALAU-DEL-VIDRE"/>
        <value key="PASSA" value="PASSA"/>
        <value key="PERPIGNAN" value="PERPIGNAN"/>
        <value key="PEYRESTORTES" value="PEYRESTORTES"/>
        <value key="PEZILLA-LA-RIVIERE" value="PEZILLA-LA-RIVIERE"/>
        <value key="PIA" value="PIA"/>
        <value key="POLLESTRES" value="POLLESTRES"/>
        <value key="PONTEILLA" value="PONTEILLA"/>
        <value key="RIVESALTES" value="RIVESALTES"/>
        <value key="SAINT-ANDRE" value="SAINT-ANDRE"/>
        <value key="SAINT-CYPRIEN" value="SAINT-CYPRIEN"/>
        <value key="SAINT-ESTEVE" value="SAINT-ESTEVE"/>
        <value key="SAINT-FELIU-D-AMONT" value="SAINT-FELIU-D-AMONT"/>
        <value key="SAINT-FELIU-D-AVALL" value="SAINT-FELIU-D-AVALL"/>
        <value key="SAINT-GENIS-DES-FONTAINES" value="SAINT-GENIS-DES-FONTAINES"/>
        <value key="SAINT-HIPPOLYTE" value="SAINT-HIPPOLYTE"/>
        <value key="SAINT-JEAN-LASSEILLE" value="SAINT-JEAN-LASSEILLE"/>
        <value key="SAINT-JEAN-PLA-DE-CORTS" value="SAINT-JEAN-PLA-DE-CORTS"/>
        <value key="SAINT-LAURENT-DE-LA-SALANQUE" value="SAINT-LAURENT-DE-LA-SALANQUE"/>
        <value key="SAINT-MICHEL-DE-LLOTES" value="SAINT-MICHEL-DE-LLOTES"/>
        <value key="SAINT-NAZAIRE" value="SAINT-NAZAIRE"/>
        <value key="SAINTE-COLOMBE-DE-LA-COMMANDERIE" value="SAINTE-COLOMBE-DE-LA-COMMANDERIE"/>
        <value key="SAINTE-MARIE" value="SAINTE-MARIE"/>
        <value key="SALEILLES" value="SALEILLES"/>
        <value key="SALSES-LE-CHATEAU" value="SALSES-LE-CHATEAU"/>
        <value key="SOREDE" value="SOREDE"/>
        <value key="TERRATS" value="TERRATS"/>
        <value key="THEZA" value="THEZA"/>
        <value key="THUIR" value="THUIR"/>
        <value key="TORDERES" value="TORDERES"/>
        <value key="TORREILLES" value="TORREILLES"/>
        <value key="TOULOUGES" value="TOULOUGES"/>
        <value key="TRESSERRE" value="TRESSERRE"/>
        <value key="TROUILLAS" value="TROUILLAS"/>
        <value key="VILLELONGUE-DE-LA-SALANQUE" value="VILLELONGUE-DE-LA-SALANQUE"/>
        <value key="VILLELONGUE-DELS-MONTS" value="VILLELONGUE-DELS-MONTS"/>
        <value key="VILLEMOLAQUE" value="VILLEMOLAQUE"/>
        <value key="VILLENEUVE-DE-LA-RAHO" value="VILLENEUVE-DE-LA-RAHO"/>
        <value key="VILLENEUVE-LA-RIVIERE" value="VILLENEUVE-LA-RIVIERE"/>
        <value key="VIVES" value="VIVES"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="SECTION">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="PARCELLE">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="LIEU_DIT">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="UG_EVP">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="Agly-Salanque" value="Agly-Salanque"/>
        <value key="Aspres-Réart" value="Aspres-Réart"/>
        <value key="Bordure Côtière Nord" value="Bordure Côtière Nord"/>
        <value key="Bordure Côtière Sud" value="Bordure Côtière Sud"/>
        <value key="Vallée de la Têt" value="Vallée de la Têt"/>
        <value key="Vallée du Tech" value="Vallée du Tech"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="HYDRIAD">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="SOURCE_DIV">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_AERMC">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_BSS">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_BSS17">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_ARS">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_DDTM">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_DREAL">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="CODE_AGRI">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_JOUR_DDT">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_MOIS_DDT">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_AN_DDT">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_JOUR_CA">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_AN_CA">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="Q_M3H_ARS">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_JOUR_ARS">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="V_AN_ARS">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="COMPTAGE">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="" value="{2839923C-8B7D-419E-B84B-CA2FE9B80EC7}"/>
        <value key="ADIS" value="ADIS"/>
        <value key="Compteur" value="Compteur"/>
        <value key="Forfait" value="Forfait"/>
        <value key="Ordinateur de serre" value="Ordinateur de serre"/>
        <value key="Tps fonctionnement pompe" value="Tps fonctionnement pompe"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="TextEdit" name="Q_POMP_M3H">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="AUTOR_DDTM">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="MO_NOM">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="MO_CONTACT">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="REMARQUES">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ValueMap" name="VERIF_TERR">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="" value="{2839923C-8B7D-419E-B84B-CA2FE9B80EC7}"/>
        <value key="Non trouvé" value="Non trouvé"/>
        <value key="Non vérifié" value="Non vérifié"/>
        <value key="Vérifié autre" value="Vérifié autre"/>
        <value key="Vérifié par SM" value="Vérifié par SM"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="ValueMap" name="FOREUR">
      <widgetv2config fieldEditable="1" constraint="" labelOnTop="0" constraintDescription="" notNull="0">
        <value key="" value="{2839923C-8B7D-419E-B84B-CA2FE9B80EC7}"/>
        <value key="AD FORAGE" value="AD FORAGE"/>
        <value key="ALLO FORAGE" value="ALLO FORAGE"/>
        <value key="AQUA FORAGE" value="AQUA FORAGE"/>
        <value key="BACHY FORAGE" value="BACHY FORAGE"/>
        <value key="BELLMAS" value="BELLMAS"/>
        <value key="BONIFACE" value="BONIFACE"/>
        <value key="COLL" value="COLL"/>
        <value key="FOREUR ESPAGNOL" value="FOREUR ESPAGNOL"/>
        <value key="FRANCE FORAGE" value="FRANCE FORAGE"/>
        <value key="GARCIA" value="GARCIA"/>
        <value key="LANDRIC" value="LANDRIC"/>
        <value key="MARLY PAUL" value="MARLY PAUL"/>
        <value key="MASSE FORAGE" value="MASSE FORAGE"/>
        <value key="MIAS PÈRE" value="MIAS PÈRE"/>
        <value key="MONTAVON" value="MONTAVON"/>
        <value key="PARTICULIER" value="PARTICULIER"/>
        <value key="PIMENTEL BTP SARL" value="PIMENTEL BTP SARL"/>
        <value key="ROUSSILLON FORAGE" value="ROUSSILLON FORAGE"/>
        <value key="SADE" value="SADE"/>
        <value key="SERIC FORAGE" value="SERIC FORAGE"/>
        <value key="SLB FORAGE" value="SLB FORAGE"/>
        <value key="SUD OUEST FORAGE" value="SUD OUEST FORAGE"/>
      </widgetv2config>
    </edittype>
    <edittype widgetv2type="DateTime" name="DATE_AJOUT">
      <widgetv2config fieldEditable="1" calendar_popup="0" allow_null="1" display_format="dd/MM/yyyy" field_format="yyyy-MM-dd" constraint="" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="DateTime" name="DATE_MODIF">
      <widgetv2config fieldEditable="1" calendar_popup="0" allow_null="1" display_format="dd/MM/yyyy" field_format="yyyy-MM-dd" constraint="" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="ExternalResource" name="DOCUMENTS">
      <widgetv2config fieldEditable="1" DocumentViewer="0" FileWidgetButton="0" UseLink="1" FullUrl="1" constraint="" FileWidget="1" StorageMode="0" labelOnTop="0" constraintDescription="" notNull="0" FileWidgetFilter=""/>
    </edittype>
    <edittype widgetv2type="ExternalResource" name="LIEN_PHOTO">
      <widgetv2config fieldEditable="1" DocumentViewer="1" FileWidgetButton="1" DocumentViewerWidth="0" constraint="" FileWidget="0" DocumentViewerHeight="0" StorageMode="0" labelOnTop="0" constraintDescription="" notNull="0" FileWidgetFilter=""/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="LIEN_IGN">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="DATE_HGA">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="DATE_AUTOR">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="DATE_DUP">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="AVIS_HGA">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="AUTO_PREF">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="EXPLO_MODE">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="EXPLO_NOM">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
    <edittype widgetv2type="TextEdit" name="EXPLO_TEL">
      <widgetv2config IsMultiline="0" fieldEditable="1" constraint="" UseHtml="0" labelOnTop="0" constraintDescription="" notNull="0"/>
    </edittype>
  </edittypes>
  <renderer-v2 forceraster="0" symbollevels="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol alpha="1" clip_to_extent="1" type="marker" name="0">
        <layer pass="0" class="SimpleMarker" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="area"/>
          <prop k="size" v="3"/>
          <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale scalemethod="diameter"/>
  </renderer-v2>
  <labeling type="simple"/>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="labeling" value="pal"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="true"/>
    <property key="labeling/bufferJoinStyle" value="128"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="2"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidInside" value="false"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/decimals" value="3"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="0"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/distMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/drawLabels" value="true"/>
    <property key="labeling/enabled" value="true"/>
    <property key="labeling/fieldName" value="'N° Ouvrage : '  || &quot;NUM_OUVR&quot;   ||  '\n'  || &#xd;&#xa;'Nom ouvrage : '  || &quot;NOM_OUVR&quot; ||  '\n'  || &#xd;&#xa;'Nappe captée : '  || &quot;NAPPE&quot; ||  '\n'  || &#xd;&#xa;'Profondeur (m) : '  || &quot;PROF_M&quot; ||  '\n' || &#xd;&#xa;'Usage : '  || &quot;USAGES&quot;"/>
    <property key="labeling/fitInPolygonOnly" value="false"/>
    <property key="labeling/fontCapitals" value="1"/>
    <property key="labeling/fontFamily" value="MS Shell Dlg 2"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="8.25"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="50"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="true"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="25"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-25"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="0"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Normal"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/obstacleFactor" value="1"/>
    <property key="labeling/obstacleType" value="0"/>
    <property key="labeling/offsetType" value="0"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="0"/>
    <property key="labeling/placementFlags" value="10"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/predefinedPositionOrder" value="TR,TL,BR,BL,R,L,TSR,BSR"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/repeatDistance" value="0"/>
    <property key="labeling/repeatDistanceMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/repeatDistanceUnit" value="1"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="7500"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="true"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/substitutions" value="&lt;substitutions/>"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="0"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/useSubstitutions" value="false"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
    <property key="labeling/zIndex" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerTransparency>0</layerTransparency>
  <displayfield>NUM_OUVR</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Étiquette"/>
    <family fieldname="" name="MS Shell Dlg 2"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <SingleCategoryDiagramRenderer diagramType="Histogram" sizeLegend="0" attributeLegend="1">
    <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" sizeScale="0,0,0,0,0,0" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" lineSizeScale="0,0,0,0,0,0" sizeType="MM" lineSizeType="MM" minScaleDenominator="inf">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
    <symbol alpha="1" clip_to_extent="1" type="marker" name="sizeSymbol">
      <layer pass="0" class="SimpleMarker" locked="0">
        <prop k="angle" v="0"/>
        <prop k="color" v="255,0,0,255"/>
        <prop k="horizontal_anchor_point" v="1"/>
        <prop k="joinstyle" v="bevel"/>
        <prop k="name" v="circle"/>
        <prop k="offset" v="0,0"/>
        <prop k="offset_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="offset_unit" v="MM"/>
        <prop k="outline_color" v="0,0,0,255"/>
        <prop k="outline_style" v="solid"/>
        <prop k="outline_width" v="0"/>
        <prop k="outline_width_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="outline_width_unit" v="MM"/>
        <prop k="scale_method" v="diameter"/>
        <prop k="size" v="2"/>
        <prop k="size_map_unit_scale" v="0,0,0,0,0,0"/>
        <prop k="size_unit" v="MM"/>
        <prop k="vertical_anchor_point" v="1"/>
      </layer>
    </symbol>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings yPosColumn="-1" showColumn="-1" linePlacementFlags="10" placement="0" dist="0" xPosColumn="-1" priority="0" obstacle="0" zIndex="0" showAll="1"/>
  <annotationform></annotationform>
  <aliases>
    <alias field="NUM_OUVR" index="0" name=""/>
    <alias field="NOM_OUVR" index="1" name=""/>
    <alias field="TYPE_OUVR" index="2" name=""/>
    <alias field="PROF_M" index="3" name=""/>
    <alias field="PROF_MESUR" index="4" name=""/>
    <alias field="NAPPE" index="5" name=""/>
    <alias field="NAT_TUBAGE" index="6" name=""/>
    <alias field="DIAM_MM" index="7" name=""/>
    <alias field="COUPE_GEOL" index="8" name=""/>
    <alias field="COUPE_TECH" index="9" name=""/>
    <alias field="USAGES" index="10" name=""/>
    <alias field="ETAT" index="11" name=""/>
    <alias field="DATE_OUVR" index="12" name=""/>
    <alias field="X_L93" index="13" name=""/>
    <alias field="Y_L93" index="14" name=""/>
    <alias field="LONG_WGS84" index="15" name=""/>
    <alias field="LAT_WGS84" index="16" name=""/>
    <alias field="Z_M" index="17" name=""/>
    <alias field="QUALIT_LOC" index="18" name=""/>
    <alias field="CORREC_LOC" index="19" name=""/>
    <alias field="Z_PRECIS" index="20" name=""/>
    <alias field="COMMUNE" index="21" name=""/>
    <alias field="SECTION" index="22" name=""/>
    <alias field="PARCELLE" index="23" name=""/>
    <alias field="LIEU_DIT" index="24" name=""/>
    <alias field="UG_EVP" index="25" name=""/>
    <alias field="HYDRIAD" index="26" name=""/>
    <alias field="SOURCE_DIV" index="27" name=""/>
    <alias field="CODE_AERMC" index="28" name=""/>
    <alias field="CODE_BSS" index="29" name=""/>
    <alias field="CODE_BSS17" index="30" name=""/>
    <alias field="CODE_ARS" index="31" name=""/>
    <alias field="CODE_DDTM" index="32" name=""/>
    <alias field="CODE_DREAL" index="33" name=""/>
    <alias field="CODE_AGRI" index="34" name=""/>
    <alias field="V_JOUR_DDT" index="35" name=""/>
    <alias field="V_MOIS_DDT" index="36" name=""/>
    <alias field="V_AN_DDT" index="37" name=""/>
    <alias field="V_JOUR_CA" index="38" name=""/>
    <alias field="V_AN_CA" index="39" name=""/>
    <alias field="Q_M3H_ARS" index="40" name=""/>
    <alias field="V_JOUR_ARS" index="41" name=""/>
    <alias field="V_AN_ARS" index="42" name=""/>
    <alias field="COMPTAGE" index="43" name=""/>
    <alias field="Q_POMP_M3H" index="44" name=""/>
    <alias field="AUTOR_DDTM" index="45" name=""/>
    <alias field="MO_NOM" index="46" name=""/>
    <alias field="MO_CONTACT" index="47" name=""/>
    <alias field="REMARQUES" index="48" name=""/>
    <alias field="VERIF_TERR" index="49" name=""/>
    <alias field="FOREUR" index="50" name=""/>
    <alias field="DATE_AJOUT" index="51" name=""/>
    <alias field="DATE_MODIF" index="52" name=""/>
    <alias field="DOCUMENTS" index="53" name=""/>
    <alias field="LIEN_PHOTO" index="54" name=""/>
    <alias field="LIEN_IGN" index="55" name=""/>
    <alias field="DATE_HGA" index="56" name=""/>
    <alias field="DATE_AUTOR" index="57" name=""/>
    <alias field="DATE_DUP" index="58" name=""/>
    <alias field="AVIS_HGA" index="59" name=""/>
    <alias field="AUTO_PREF" index="60" name=""/>
    <alias field="EXPLO_MODE" index="61" name=""/>
    <alias field="EXPLO_NOM" index="62" name=""/>
    <alias field="EXPLO_TEL" index="63" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <attributeactions default="-1"/>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="&quot;DATE_MODIF&quot;" sortOrder="0">
    <columns>
      <column width="-1" hidden="0" type="field" name="NUM_OUVR"/>
      <column width="306" hidden="0" type="field" name="NOM_OUVR"/>
      <column width="-1" hidden="0" type="field" name="TYPE_OUVR"/>
      <column width="-1" hidden="0" type="field" name="PROF_M"/>
      <column width="-1" hidden="0" type="field" name="PROF_MESUR"/>
      <column width="-1" hidden="0" type="field" name="NAPPE"/>
      <column width="-1" hidden="0" type="field" name="NAT_TUBAGE"/>
      <column width="-1" hidden="0" type="field" name="DIAM_MM"/>
      <column width="-1" hidden="0" type="field" name="COUPE_GEOL"/>
      <column width="-1" hidden="0" type="field" name="COUPE_TECH"/>
      <column width="-1" hidden="0" type="field" name="USAGES"/>
      <column width="-1" hidden="0" type="field" name="ETAT"/>
      <column width="-1" hidden="0" type="field" name="DATE_OUVR"/>
      <column width="-1" hidden="0" type="field" name="X_L93"/>
      <column width="-1" hidden="0" type="field" name="Y_L93"/>
      <column width="-1" hidden="0" type="field" name="LONG_WGS84"/>
      <column width="-1" hidden="0" type="field" name="LAT_WGS84"/>
      <column width="-1" hidden="0" type="field" name="Z_M"/>
      <column width="-1" hidden="0" type="field" name="QUALIT_LOC"/>
      <column width="-1" hidden="0" type="field" name="CORREC_LOC"/>
      <column width="-1" hidden="0" type="field" name="Z_PRECIS"/>
      <column width="-1" hidden="0" type="field" name="COMMUNE"/>
      <column width="-1" hidden="0" type="field" name="SECTION"/>
      <column width="-1" hidden="0" type="field" name="PARCELLE"/>
      <column width="-1" hidden="0" type="field" name="LIEU_DIT"/>
      <column width="110" hidden="0" type="field" name="UG_EVP"/>
      <column width="-1" hidden="0" type="field" name="HYDRIAD"/>
      <column width="-1" hidden="0" type="field" name="SOURCE_DIV"/>
      <column width="-1" hidden="0" type="field" name="CODE_AERMC"/>
      <column width="-1" hidden="0" type="field" name="CODE_BSS"/>
      <column width="-1" hidden="0" type="field" name="CODE_BSS17"/>
      <column width="-1" hidden="0" type="field" name="CODE_ARS"/>
      <column width="-1" hidden="0" type="field" name="CODE_DDTM"/>
      <column width="-1" hidden="0" type="field" name="CODE_DREAL"/>
      <column width="-1" hidden="0" type="field" name="CODE_AGRI"/>
      <column width="-1" hidden="0" type="field" name="V_JOUR_DDT"/>
      <column width="-1" hidden="0" type="field" name="V_MOIS_DDT"/>
      <column width="-1" hidden="0" type="field" name="V_AN_DDT"/>
      <column width="-1" hidden="0" type="field" name="V_JOUR_CA"/>
      <column width="-1" hidden="0" type="field" name="V_AN_CA"/>
      <column width="-1" hidden="0" type="field" name="Q_M3H_ARS"/>
      <column width="-1" hidden="0" type="field" name="V_JOUR_ARS"/>
      <column width="-1" hidden="0" type="field" name="V_AN_ARS"/>
      <column width="-1" hidden="0" type="field" name="COMPTAGE"/>
      <column width="-1" hidden="0" type="field" name="Q_POMP_M3H"/>
      <column width="-1" hidden="0" type="field" name="AUTOR_DDTM"/>
      <column width="-1" hidden="0" type="field" name="MO_NOM"/>
      <column width="-1" hidden="0" type="field" name="MO_CONTACT"/>
      <column width="-1" hidden="0" type="field" name="REMARQUES"/>
      <column width="-1" hidden="0" type="field" name="VERIF_TERR"/>
      <column width="-1" hidden="0" type="field" name="FOREUR"/>
      <column width="-1" hidden="0" type="field" name="DATE_AJOUT"/>
      <column width="-1" hidden="0" type="field" name="DATE_MODIF"/>
      <column width="467" hidden="0" type="field" name="DOCUMENTS"/>
      <column width="-1" hidden="0" type="field" name="LIEN_PHOTO"/>
      <column width="-1" hidden="0" type="field" name="LIEN_IGN"/>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" hidden="0" type="field" name="DATE_HGA"/>
      <column width="-1" hidden="0" type="field" name="DATE_AUTOR"/>
      <column width="-1" hidden="0" type="field" name="DATE_DUP"/>
      <column width="-1" hidden="0" type="field" name="AVIS_HGA"/>
      <column width="-1" hidden="0" type="field" name="AUTO_PREF"/>
      <column width="-1" hidden="0" type="field" name="EXPLO_MODE"/>
      <column width="-1" hidden="0" type="field" name="EXPLO_NOM"/>
      <column width="-1" hidden="0" type="field" name="EXPLO_TEL"/>
    </columns>
  </attributetableconfig>
  <editform></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>tablayout</editorlayout>
  <attributeEditorForm>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Ouvrage" groupBox="0" columnCount="1">
      <attributeEditorField showLabel="1" index="0" name="NUM_OUVR"/>
      <attributeEditorField showLabel="1" index="1" name="NOM_OUVR"/>
      <attributeEditorField showLabel="1" index="2" name="TYPE_OUVR"/>
      <attributeEditorField showLabel="1" index="3" name="PROF_M"/>
      <attributeEditorField showLabel="1" index="5" name="NAPPE"/>
      <attributeEditorField showLabel="1" index="12" name="DATE_OUVR"/>
      <attributeEditorField showLabel="1" index="10" name="USAGES"/>
      <attributeEditorField showLabel="1" index="50" name="FOREUR"/>
      <attributeEditorField showLabel="1" index="11" name="ETAT"/>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Photo" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="0" index="54" name="LIEN_PHOTO"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Infos techniques" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Données" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="3" name="PROF_M"/>
        <attributeEditorField showLabel="1" index="6" name="NAT_TUBAGE"/>
        <attributeEditorField showLabel="1" index="7" name="DIAM_MM"/>
        <attributeEditorField showLabel="1" index="8" name="COUPE_GEOL"/>
        <attributeEditorField showLabel="1" index="9" name="COUPE_TECH"/>
        <attributeEditorField showLabel="1" index="44" name="Q_POMP_M3H"/>
        <attributeEditorField showLabel="1" index="43" name="COMPTAGE"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Mesures terrain" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="49" name="VERIF_TERR"/>
        <attributeEditorField showLabel="1" index="4" name="PROF_MESUR"/>
        <attributeEditorField showLabel="1" index="-1" name="COMPTEUR"/>
        <attributeEditorField showLabel="1" index="-1" name="CLAPET"/>
        <attributeEditorField showLabel="1" index="-1" name="MARGELLE"/>
        <attributeEditorField showLabel="1" index="-1" name="PROTECTION"/>
        <attributeEditorField showLabel="1" index="-1" name="HAUT_TETE"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Sources" groupBox="0" columnCount="1">
      <attributeEditorField showLabel="1" index="28" name="CODE_AERMC"/>
      <attributeEditorField showLabel="1" index="29" name="CODE_BSS"/>
      <attributeEditorField showLabel="1" index="30" name="CODE_BSS17"/>
      <attributeEditorField showLabel="1" index="31" name="CODE_ARS"/>
      <attributeEditorField showLabel="1" index="32" name="CODE_DDTM"/>
      <attributeEditorField showLabel="1" index="33" name="CODE_DREAL"/>
      <attributeEditorField showLabel="1" index="34" name="CODE_AGRI"/>
      <attributeEditorField showLabel="1" index="27" name="SOURCE_DIV"/>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Localisation" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Implantation" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="25" name="UG_EVP"/>
        <attributeEditorField showLabel="1" index="21" name="COMMUNE"/>
        <attributeEditorField showLabel="1" index="22" name="SECTION"/>
        <attributeEditorField showLabel="1" index="23" name="PARCELLE"/>
        <attributeEditorField showLabel="1" index="24" name="LIEU_DIT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Coordonnées" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="13" name="X_L93"/>
        <attributeEditorField showLabel="1" index="14" name="Y_L93"/>
        <attributeEditorField showLabel="1" index="15" name="LONG_WGS84"/>
        <attributeEditorField showLabel="1" index="16" name="LAT_WGS84"/>
        <attributeEditorField showLabel="1" index="18" name="QUALIT_LOC"/>
        <attributeEditorField showLabel="1" index="19" name="CORREC_LOC"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Altitude" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="17" name="Z_M"/>
        <attributeEditorField showLabel="1" index="20" name="Z_PRECIS"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Autorisations" groupBox="0" columnCount="1">
      <attributeEditorField showLabel="1" index="45" name="AUTOR_DDTM"/>
      <attributeEditorField showLabel="1" index="57" name="DATE_AUTOR"/>
      <attributeEditorField showLabel="1" index="58" name="DATE_DUP"/>
      <attributeEditorField showLabel="1" index="60" name="AUTO_PREF"/>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Volumes déclarés/autorisés" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="DDTM" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="35" name="V_JOUR_DDT"/>
        <attributeEditorField showLabel="1" index="36" name="V_MOIS_DDT"/>
        <attributeEditorField showLabel="1" index="37" name="V_AN_DDT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="ARS" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="40" name="Q_M3H_ARS"/>
        <attributeEditorField showLabel="1" index="41" name="V_JOUR_ARS"/>
        <attributeEditorField showLabel="1" index="42" name="V_AN_ARS"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="CH-AGRI" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="38" name="V_JOUR_CA"/>
        <attributeEditorField showLabel="1" index="39" name="V_AN_CA"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Maitre d'ouvrage" groupBox="0" columnCount="1">
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Maitre d'ouvrage" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="46" name="MO_NOM"/>
        <attributeEditorField showLabel="1" index="47" name="MO_CONTACT"/>
      </attributeEditorContainer>
      <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Exploitant" groupBox="1" columnCount="1">
        <attributeEditorField showLabel="1" index="61" name="EXPLO_MODE"/>
        <attributeEditorField showLabel="1" index="62" name="EXPLO_NOM"/>
        <attributeEditorField showLabel="1" index="63" name="EXPLO_TEL"/>
      </attributeEditorContainer>
    </attributeEditorContainer>
    <attributeEditorContainer showLabel="1" visibilityExpressionEnabled="0" visibilityExpression="" name="Infos BD" groupBox="0" columnCount="1">
      <attributeEditorField showLabel="1" index="48" name="REMARQUES"/>
      <attributeEditorField showLabel="1" index="51" name="DATE_AJOUT"/>
      <attributeEditorField showLabel="1" index="52" name="DATE_MODIF"/>
      <attributeEditorField showLabel="1" index="53" name="DOCUMENTS"/>
      <attributeEditorField showLabel="1" index="54" name="LIEN_PHOTO"/>
      <attributeEditorField showLabel="1" index="55" name="LIEN_IGN"/>
    </attributeEditorContainer>
  </attributeEditorForm>
  <widgets/>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <defaults>
    <default field="NUM_OUVR" expression=""/>
    <default field="NOM_OUVR" expression=""/>
    <default field="TYPE_OUVR" expression=""/>
    <default field="PROF_M" expression=""/>
    <default field="PROF_MESUR" expression=""/>
    <default field="NAPPE" expression=""/>
    <default field="NAT_TUBAGE" expression=""/>
    <default field="DIAM_MM" expression=""/>
    <default field="COUPE_GEOL" expression=""/>
    <default field="COUPE_TECH" expression=""/>
    <default field="USAGES" expression=""/>
    <default field="ETAT" expression=""/>
    <default field="DATE_OUVR" expression=""/>
    <default field="X_L93" expression=""/>
    <default field="Y_L93" expression=""/>
    <default field="LONG_WGS84" expression=""/>
    <default field="LAT_WGS84" expression=""/>
    <default field="Z_M" expression=""/>
    <default field="QUALIT_LOC" expression=""/>
    <default field="CORREC_LOC" expression=""/>
    <default field="Z_PRECIS" expression=""/>
    <default field="COMMUNE" expression=""/>
    <default field="SECTION" expression=""/>
    <default field="PARCELLE" expression=""/>
    <default field="LIEU_DIT" expression=""/>
    <default field="UG_EVP" expression=""/>
    <default field="HYDRIAD" expression=""/>
    <default field="SOURCE_DIV" expression=""/>
    <default field="CODE_AERMC" expression=""/>
    <default field="CODE_BSS" expression=""/>
    <default field="CODE_BSS17" expression=""/>
    <default field="CODE_ARS" expression=""/>
    <default field="CODE_DDTM" expression=""/>
    <default field="CODE_DREAL" expression=""/>
    <default field="CODE_AGRI" expression=""/>
    <default field="V_JOUR_DDT" expression=""/>
    <default field="V_MOIS_DDT" expression=""/>
    <default field="V_AN_DDT" expression=""/>
    <default field="V_JOUR_CA" expression=""/>
    <default field="V_AN_CA" expression=""/>
    <default field="Q_M3H_ARS" expression=""/>
    <default field="V_JOUR_ARS" expression=""/>
    <default field="V_AN_ARS" expression=""/>
    <default field="COMPTAGE" expression=""/>
    <default field="Q_POMP_M3H" expression=""/>
    <default field="AUTOR_DDTM" expression=""/>
    <default field="MO_NOM" expression=""/>
    <default field="MO_CONTACT" expression=""/>
    <default field="REMARQUES" expression=""/>
    <default field="VERIF_TERR" expression=""/>
    <default field="FOREUR" expression=""/>
    <default field="DATE_AJOUT" expression=""/>
    <default field="DATE_MODIF" expression=""/>
    <default field="DOCUMENTS" expression=""/>
    <default field="LIEN_PHOTO" expression=""/>
    <default field="LIEN_IGN" expression=""/>
    <default field="DATE_HGA" expression=""/>
    <default field="DATE_AUTOR" expression=""/>
    <default field="DATE_DUP" expression=""/>
    <default field="AVIS_HGA" expression=""/>
    <default field="AUTO_PREF" expression=""/>
    <default field="EXPLO_MODE" expression=""/>
    <default field="EXPLO_NOM" expression=""/>
    <default field="EXPLO_TEL" expression=""/>
  </defaults>
  <previewExpression>COALESCE( "NUM_OUVR", '&lt;NULL>' )</previewExpression>
  <layerGeometryType>0</layerGeometryType>
</qgis>
