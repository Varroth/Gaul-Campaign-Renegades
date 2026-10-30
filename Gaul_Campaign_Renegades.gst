<?xml version='1.0' encoding='UTF-8'?>
<gameSystem xmlns="http://www.battlescribe.net/schema/gameSystemSchema" id="0408-b3dc-97f0-53dc" name="Gaul Campaign: Renegades" revision="7" battleScribeVersion="2.03">
  <costTypes>
    <costType id="0246-3343-a75c-5ffa" name="pts" defaultCostLimit="-1.0" hidden="false"/>
    <costType id="6c3b-5f19-3bc2-5dbb" name="DP" defaultCostLimit="3.0" hidden="false"/>
  </costTypes>
  <profileTypes>
    <profileType id="0cb1-7394-fb88-5322" name="Unit">
      <characteristicTypes>
        <characteristicType id="8ffa-8367-2184-5557" name="M"/>
        <characteristicType id="c2bc-ad63-c63b-5cea" name="T"/>
        <characteristicType id="f078-5176-43c6-5f6a" name="Sv"/>
        <characteristicType id="ecdc-11e1-15d1-5780" name="W"/>
        <characteristicType id="2bb6-cceb-9d3f-5f47" name="Ld"/>
        <characteristicType id="6bb9-f7e0-3ec4-5517" name="OC"/>
      </characteristicTypes>
    </profileType>
    <profileType id="bd5c-f804-35b5-510d" name="Ability">
      <characteristicTypes>
        <characteristicType id="4c71-0d90-3b92-5cec" name="Description"/>
      </characteristicTypes>
    </profileType>
    <profileType id="a4f5-4674-06d7-5496" name="Weapon">
      <characteristicTypes>
        <characteristicType id="8aa7-21a6-b6c1-50e6" name="Range"/>
        <characteristicType id="1df3-e803-7074-57ce" name="A"/>
        <characteristicType id="a16c-0b6c-2681-5f8f" name="BS/WS"/>
        <characteristicType id="846d-1dce-303c-5c75" name="S"/>
        <characteristicType id="91f2-51a2-9429-5a60" name="AP"/>
        <characteristicType id="14cd-2ade-2ccc-5c11" name="D"/>
        <characteristicType id="0f05-4353-204c-511f" name="Traits"/>
      </characteristicTypes>
    </profileType>
  </profileTypes>
  <categoryEntries>
    <categoryEntry id="b411-6717-d966-5c6d" name="Command" hidden="false"/>
    <categoryEntry id="ec2c-68bb-bfbc-5ee3" name="Battleline" hidden="false"/>
    <categoryEntry id="521d-dd50-6a49-58fb" name="Infantry" hidden="false"/>
    <categoryEntry id="a7ac-6dda-f2f1-5ba4" name="Elites" hidden="false"/>
    <categoryEntry id="c317-a497-01c6-5b78" name="Terminators" hidden="false"/>
    <categoryEntry id="2a7b-0016-ba81-5ad6" name="Jump Infantry" hidden="false"/>
    <categoryEntry id="bf60-94d3-7c97-5f42" name="Mounted" hidden="false"/>
    <categoryEntry id="93a3-7ba9-2915-5ea2" name="Mortal Auxilia" hidden="false"/>
    <categoryEntry id="930f-f4e6-1451-52ba" name="Dreadnoughts" hidden="false"/>
    <categoryEntry id="693a-223d-bdae-5cbb" name="Vehicles" hidden="false"/>
    <categoryEntry id="9856-3547-9660-54c2" name="Transports" hidden="false"/>
    <categoryEntry id="6be8-bd06-032f-5209" name="Aircraft" hidden="false"/>
    <categoryEntry id="4a72-54d4-f63a-5086" name="Artillery" hidden="false"/>
    <categoryEntry id="b703-ed42-a968-5cce" name="Daemon Engines" hidden="false"/>
    <categoryEntry id="471b-b5c6-68a0-523c" name="Khorne Allies" hidden="false"><constraints><constraint id="6d33efc5-a834-459e" type="max" field="0246-3343-a75c-5ffa" scope="roster" value="500" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true"/></constraints><modifiers><modifier type="set" field="6d33efc5-a834-459e" value="250"><conditions><condition type="atLeast" value="1" field="selections" scope="roster" childId="b5e1b5c6-826e-48dd" shared="true" includeChildSelections="true" includeChildForces="true"/></conditions></modifier></modifiers></categoryEntry>
    <categoryEntry id="2962-6989-212f-598d" name="Lost Cohort" hidden="false"><constraints><constraint id="5fb20465-2d7f-49e5" type="max" field="selections" scope="roster" value="2" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/></constraints></categoryEntry>
    <categoryEntry id="3c17-c261-4038-5fcc" name="Detachments" hidden="false"/>
    <categoryEntry id="40b7-29b0-a885-5757" name="Enhancements" hidden="false"/>
  <categoryEntry id="9bc4-2501-1ea8-5f22" name="Muster Settings" hidden="false"><constraints><constraint id="a3e0bc94-56c6-4d15-87d4-6b41feb1bd3f" type="min" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/><constraint id="3f4ebc3c-5ba2-461e-81a6-6a561ac06f4b" type="max" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/></constraints></categoryEntry><categoryEntry id="b9f3-c313-59f0-5cef" name="Force Dispositions" hidden="false"><constraints><constraint id="27269594-7e74-4e70-9240-6c5e27ac21fc" type="min" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/><constraint id="bee1fe7f-89cc-40d6-a168-28d4f8f8a166" type="max" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/></constraints></categoryEntry><categoryEntry id="524e-6fc1-14f9-5aa1" name="Configuration Tools" hidden="false"/>    <categoryEntry id="adbd-c48e-4b21-0002" name="Specialists" hidden="false"/>
    <categoryEntry id="adbd-c48e-4b21-0003" name="Vehicles &amp; Support" hidden="false"/>
    <categoryEntry id="adbd-c48e-4b21-a001" name="ASTARTES" hidden="false"/>
    <categoryEntry id="adbd-c48e-4b21-a002" name="DIRECTORATE" hidden="false"/>
    <categoryEntry id="adbd-c48e-4b21-a003" name="CULTISTS" hidden="false"/>
  </categoryEntries>
  <forceEntries>
    <forceEntry id="73a9-6482-df85-55c4" name="Infernal Warriors Muster" hidden="false">
      <categoryLinks>
        <categoryLink id="96d4-3d87-baa5-5281" name="Command" hidden="false" targetId="b411-6717-d966-5c6d" primary="false"/>
        <categoryLink id="bec9-e84b-e7d4-52e8" name="Battleline" hidden="false" targetId="ec2c-68bb-bfbc-5ee3" primary="false"/>
        <categoryLink id="66b5-a647-bfc5-5c90" name="Infantry" hidden="false" targetId="521d-dd50-6a49-58fb" primary="false"/>
        <categoryLink id="ea86-31c2-f095-517b" name="Elites" hidden="false" targetId="a7ac-6dda-f2f1-5ba4" primary="false"/>
        <categoryLink id="894a-51a2-aa5a-54a4" name="Terminators" hidden="false" targetId="c317-a497-01c6-5b78" primary="false"/>
        <categoryLink id="26be-fc95-3d8a-5aa0" name="Jump Infantry" hidden="false" targetId="2a7b-0016-ba81-5ad6" primary="false"/>
        <categoryLink id="cd35-8972-e4be-5750" name="Mounted" hidden="false" targetId="bf60-94d3-7c97-5f42" primary="false"/>
        <categoryLink id="eb4d-42e8-b85c-5a6c" name="Mortal Auxilia" hidden="false" targetId="93a3-7ba9-2915-5ea2" primary="false"/>
        <categoryLink id="5e7a-a931-61b3-58c4" name="Dreadnoughts" hidden="false" targetId="930f-f4e6-1451-52ba" primary="false"/>
        <categoryLink id="d30b-25c8-778b-5b64" name="Vehicles" hidden="false" targetId="693a-223d-bdae-5cbb" primary="false"/>
        <categoryLink id="b6b0-92b6-eda3-5888" name="Transports" hidden="false" targetId="9856-3547-9660-54c2" primary="false"/>
        <categoryLink id="88ea-6ee8-a69f-5e11" name="Aircraft" hidden="false" targetId="6be8-bd06-032f-5209" primary="false"/>
        <categoryLink id="2d33-f871-979c-5c4e" name="Artillery" hidden="false" targetId="4a72-54d4-f63a-5086" primary="false"/>
        <categoryLink id="8519-9461-bd3d-52e5" name="Daemon Engines" hidden="false" targetId="b703-ed42-a968-5cce" primary="false"/>
        <categoryLink id="0789-b8fe-461d-56c9" name="Khorne Allies" hidden="false" targetId="471b-b5c6-68a0-523c" primary="false"/>
        <categoryLink id="4892-9cac-0368-5f7a" name="Lost Cohort" hidden="false" targetId="2962-6989-212f-598d" primary="false">
          <constraints>
            <constraint field="selections" scope="force" value="2" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="bf50-49c8-01dd-51e6" type="max"/>
          </constraints>
        </categoryLink>
        <categoryLink id="e6f8-93ce-be97-574c" name="Detachments" hidden="false" targetId="3c17-c261-4038-5fcc" primary="false">
          <constraints>
            <constraint field="selections" scope="force" value="4" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="5093-b84b-0ec5-5181" type="max"/>
            <constraint field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="53ad-756a-e210-589f" type="min"/>
          </constraints>
        </categoryLink>
        <categoryLink id="c05e-5394-0f2c-5661" name="Enhancements" hidden="false" targetId="40b7-29b0-a885-5757" primary="false"/>
      <categoryLink id="2a5115d4-57f7-4858" name="Muster Settings" hidden="false" targetId="9bc4-2501-1ea8-5f22" primary="false"/><categoryLink id="b9ec8b0a-f05d-43c8" name="Force Dispositions" hidden="false" targetId="b9f3-c313-59f0-5cef" primary="false"/><categoryLink id="602d1e48-aeb7-41d6" name="Configuration Tools" hidden="false" targetId="524e-6fc1-14f9-5aa1" primary="false"/></categoryLinks>
    </forceEntry>
      <forceEntry id="ada1-e202-6a1d-ecad" name="Abandoned Dead Task Force" hidden="false">
      <categoryLinks>
        <categoryLink id="ad7f-0000-fcce-2026" name="Command" hidden="false" targetId="b411-6717-d966-5c6d" primary="false"/>
        <categoryLink id="ad7f-0001-fcce-2026" name="Battleline" hidden="false" targetId="ec2c-68bb-bfbc-5ee3" primary="false"/>
        <categoryLink id="ad7f-0002-fcce-2026" name="Specialists" hidden="false" targetId="adbd-c48e-4b21-0002" primary="false"/>
        <categoryLink id="ad7f-0003-fcce-2026" name="Vehicles &amp; Support" hidden="false" targetId="adbd-c48e-4b21-0003" primary="false"/>
        <categoryLink id="ad7f-0004-fcce-2026" name="ASTARTES" hidden="false" targetId="adbd-c48e-4b21-a001" primary="false"/>
        <categoryLink id="ad7f-0005-fcce-2026" name="DIRECTORATE" hidden="false" targetId="adbd-c48e-4b21-a002" primary="false"/>
        <categoryLink id="ad7f-0006-fcce-2026" name="CULTISTS" hidden="false" targetId="adbd-c48e-4b21-a003" primary="false"/>
      </categoryLinks>
    </forceEntry>
  </forceEntries>
</gameSystem>
