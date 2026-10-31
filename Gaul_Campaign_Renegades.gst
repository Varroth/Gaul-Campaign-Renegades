<?xml version='1.0' encoding='UTF-8'?>
<gameSystem xmlns="http://www.battlescribe.net/schema/gameSystemSchema" id="0408-b3dc-97f0-53dc" name="Gaul Campaign: Renegades" revision="8" battleScribeVersion="2.03">
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
      <characteristicType name="Invulnerable" id="fcc9-7d25-7e12-9146"/></characteristicTypes>
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
    <categoryEntry id="9bc4-2501-1ea8-5f22" name="Muster Settings" hidden="false"><constraints><constraint id="a3e0bc94-56c6-4d15-87d4-6b41feb1bd3f" type="min" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/><constraint id="3f4ebc3c-5ba2-461e-81a6-6a561ac06f4b" type="max" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/></constraints></categoryEntry>
    <categoryEntry id="b9f3-c313-59f0-5cef" name="Force Dispositions" hidden="false"><constraints><constraint id="27269594-7e74-4e70-9240-6c5e27ac21fc" type="min" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/><constraint id="bee1fe7f-89cc-40d6-a168-28d4f8f8a166" type="max" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true"/></constraints></categoryEntry>
    <categoryEntry id="524e-6fc1-14f9-5aa1" name="Configuration Tools" hidden="false"/>
  <categoryEntry id="adbd-c48e-4b21-0002" name="Specialists" hidden="false"/><categoryEntry id="adbd-c48e-4b21-0003" name="Vehicles &amp; Support" hidden="false"/><categoryEntry id="adbd-c48e-4b21-a001" name="ASTARTES" hidden="false"/><categoryEntry id="adbd-c48e-4b21-a002" name="DIRECTORATE" hidden="false"/><categoryEntry id="adbd-c48e-4b21-a003" name="CULTISTS" hidden="false"/><categoryEntry id="b9b4-bb20-7903-f50e" name="FC · Aerial Aces" hidden="false"/><categoryEntry id="237f-1a28-dc2b-753b" name="FC · Aircraft &amp; Gunships" hidden="false"/><categoryEntry id="5b89-f231-abc9-9294" name="FC · Armored Transports" hidden="false"/><categoryEntry id="85e4-2c59-f869-fd94" name="FC · Assault Infantry" hidden="false"/><categoryEntry id="468e-98fe-33b9-74ff" name="FC · Automata" hidden="false"/><categoryEntry id="adb6-d85c-dfb3-69ed" name="FC · Battle Tanks" hidden="false"/><categoryEntry id="6d1a-80e9-0be4-0c2e" name="FC · Battleline" hidden="false"/><categoryEntry id="70f4-8323-e145-4b4b" name="FC · Bikes &amp; Jetbikes" hidden="false"/><categoryEntry id="a4bf-93d3-cebe-53ac" name="FC · Chapter Command" hidden="false"/><categoryEntry id="2e98-8db1-b592-bebd" name="FC · Character" hidden="false"/><categoryEntry id="7d07-115c-5f16-4c3b" name="FC · Combat Engineers" hidden="false"/><categoryEntry id="7855-099c-f53c-d1e7" name="FC · Contained Daemon Engines" hidden="false"/><categoryEntry id="a75f-1881-2e1a-697a" name="FC · Dreadnoughts &amp; Living Masters" hidden="false"/><categoryEntry id="10d0-b638-38e6-f957" name="FC · Drop Assault" hidden="false"/><categoryEntry id="4184-1d40-9d16-5a7a" name="FC · Elite Siege Infantry" hidden="false"/><categoryEntry id="9198-67a8-0931-f114" name="FC · Elite Wardens" hidden="false"/><categoryEntry id="ba92-31ee-3264-a18e" name="FC · Frostbound Auxilia" hidden="false"/><categoryEntry id="e5e4-dd08-6ce4-34b7" name="Frozen Cogs" hidden="false"/><categoryEntry id="1186-3015-8b1c-a8a3" name="FC · Harmonic Conclave" hidden="false"/><categoryEntry id="df1d-4be3-b832-eddc" name="FC · Heavy Support" hidden="false"/><categoryEntry id="d640-7a85-a199-c350" name="FC · Infantry" hidden="false"/><categoryEntry id="7a83-5343-b20a-173e" name="FC · Melee Shock" hidden="false"/><categoryEntry id="994c-8bb9-1d19-a104" name="FC · Named Characters" hidden="false"/><categoryEntry id="875f-19bf-1f26-b617" name="FC · Relic Super-heavy Vehicles" hidden="false"/><categoryEntry id="fcb6-2503-af40-5e72" name="FC · Sacred Forge Support" hidden="false"/><categoryEntry id="52f6-34f0-629a-266e" name="FC · Sacred Forge Walkers" hidden="false"/><categoryEntry id="9256-e70a-2cd2-8b45" name="FC · Scouts &amp; Recon" hidden="false"/><categoryEntry id="84a9-2423-5dcb-b173" name="FC · Siege Armor" hidden="false"/><categoryEntry id="6718-fb81-5496-8416" name="FC · Siege Artillery" hidden="false"/><categoryEntry id="92bc-f579-7dc3-c5db" name="FC · Siege Assault" hidden="false"/><categoryEntry id="3ca8-5dea-f094-c6e9" name="FC · Speeders &amp; Reconnaissance" hidden="false"/><categoryEntry id="9d6e-0498-c734-3fe4" name="FC · Tactical Support" hidden="false"/><categoryEntry id="0a66-2bc3-4792-5c78" name="FC · Terminator" hidden="false"/><categoryEntry id="7560-57c6-6880-4a63" name="FC · Veterans" hidden="false"/></categoryEntries>
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
          <constraints><constraint field="selections" scope="force" value="2" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="bf50-49c8-01dd-51e6" type="max"/></constraints>
        </categoryLink>
        <categoryLink id="e6f8-93ce-be97-574c" name="Detachments" hidden="false" targetId="3c17-c261-4038-5fcc" primary="false">
          <constraints><constraint field="selections" scope="force" value="4" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="5093-b84b-0ec5-5181" type="max"/><constraint field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="53ad-756a-e210-589f" type="min"/></constraints>
        </categoryLink>
        <categoryLink id="c05e-5394-0f2c-5661" name="Enhancements" hidden="false" targetId="40b7-29b0-a885-5757" primary="false"/>
        <categoryLink id="2a5115d4-57f7-4858" name="Muster Settings" hidden="false" targetId="9bc4-2501-1ea8-5f22" primary="false"/>
        <categoryLink id="b9ec8b0a-f05d-43c8" name="Force Dispositions" hidden="false" targetId="b9f3-c313-59f0-5cef" primary="false"/>
        <categoryLink id="602d1e48-aeb7-41d6" name="Configuration Tools" hidden="false" targetId="524e-6fc1-14f9-5aa1" primary="false"/>
      </categoryLinks>
    </forceEntry>
  <forceEntry id="ada1-e202-6a1d-ecad" name="Abandoned Dead Task Force" hidden="false"><categoryLinks><categoryLink id="ad7f-0000-fcce-2026" name="Command" hidden="false" targetId="b411-6717-d966-5c6d" primary="false"/><categoryLink id="ad7f-0001-fcce-2026" name="Battleline" hidden="false" targetId="ec2c-68bb-bfbc-5ee3" primary="false"/><categoryLink id="ad7f-0002-fcce-2026" name="Specialists" hidden="false" targetId="adbd-c48e-4b21-0002" primary="false"/><categoryLink id="ad7f-0003-fcce-2026" name="Vehicles &amp; Support" hidden="false" targetId="adbd-c48e-4b21-0003" primary="false"/><categoryLink id="ad7f-0004-fcce-2026" name="ASTARTES" hidden="false" targetId="adbd-c48e-4b21-a001" primary="false"/><categoryLink id="ad7f-0005-fcce-2026" name="DIRECTORATE" hidden="false" targetId="adbd-c48e-4b21-a002" primary="false"/><categoryLink id="ad7f-0006-fcce-2026" name="CULTISTS" hidden="false" targetId="adbd-c48e-4b21-a003" primary="false"/></categoryLinks></forceEntry><forceEntry id="5513-326d-9459-9678" name="Frozen Cogs Expeditionary Force" hidden="false"><categoryLinks><categoryLink id="a146-cce7-9b19-5f0c" name="FC · Aerial Aces" hidden="false" targetId="b9b4-bb20-7903-f50e" primary="false"/><categoryLink id="9cf4-cdac-2a06-8786" name="FC · Aircraft &amp; Gunships" hidden="false" targetId="237f-1a28-dc2b-753b" primary="false"/><categoryLink id="858a-4b3a-3c8c-bf20" name="FC · Armored Transports" hidden="false" targetId="5b89-f231-abc9-9294" primary="false"/><categoryLink id="6146-c5bd-4c47-38b2" name="FC · Assault Infantry" hidden="false" targetId="85e4-2c59-f869-fd94" primary="false"/><categoryLink id="12f9-21e9-6f23-284d" name="FC · Automata" hidden="false" targetId="468e-98fe-33b9-74ff" primary="false"/><categoryLink id="e333-bc9a-f1f8-0cb7" name="FC · Battle Tanks" hidden="false" targetId="adb6-d85c-dfb3-69ed" primary="false"/><categoryLink id="72fe-0640-a349-d869" name="FC · Battleline" hidden="false" targetId="6d1a-80e9-0be4-0c2e" primary="false"/><categoryLink id="69b3-b67f-9c22-c029" name="FC · Bikes &amp; Jetbikes" hidden="false" targetId="70f4-8323-e145-4b4b" primary="false"/><categoryLink id="e3be-b986-8db9-50d3" name="FC · Chapter Command" hidden="false" targetId="a4bf-93d3-cebe-53ac" primary="false"/><categoryLink id="702c-2fa5-a3dd-baab" name="FC · Combat Engineers" hidden="false" targetId="7d07-115c-5f16-4c3b" primary="false"/><categoryLink id="b7f7-64e8-8233-0b36" name="FC · Contained Daemon Engines" hidden="false" targetId="7855-099c-f53c-d1e7" primary="false"/><categoryLink id="2f51-3614-da36-78a1" name="FC · Dreadnoughts &amp; Living Masters" hidden="false" targetId="a75f-1881-2e1a-697a" primary="false"/><categoryLink id="0df9-49cc-df15-d1c9" name="FC · Drop Assault" hidden="false" targetId="10d0-b638-38e6-f957" primary="false"/><categoryLink id="1c56-e203-4fb4-aabb" name="FC · Elite Siege Infantry" hidden="false" targetId="4184-1d40-9d16-5a7a" primary="false"/><categoryLink id="dca3-260d-b912-67ef" name="FC · Elite Wardens" hidden="false" targetId="9198-67a8-0931-f114" primary="false"/><categoryLink id="22a3-4f08-5685-44f3" name="FC · Frostbound Auxilia" hidden="false" targetId="ba92-31ee-3264-a18e" primary="false"/><categoryLink id="e4b0-4278-6738-8fa4" name="FC · Harmonic Conclave" hidden="false" targetId="1186-3015-8b1c-a8a3" primary="false"/><categoryLink id="82ed-60f1-ad6e-1377" name="FC · Heavy Support" hidden="false" targetId="df1d-4be3-b832-eddc" primary="false"/><categoryLink id="1862-4910-2230-f373" name="FC · Melee Shock" hidden="false" targetId="7a83-5343-b20a-173e" primary="false"/><categoryLink id="34de-f872-3223-278e" name="FC · Named Characters" hidden="false" targetId="994c-8bb9-1d19-a104" primary="false"/><categoryLink id="3dcb-314b-dc83-cb1b" name="FC · Relic Super-heavy Vehicles" hidden="false" targetId="875f-19bf-1f26-b617" primary="false"/><categoryLink id="09fe-0607-fde0-95e1" name="FC · Sacred Forge Support" hidden="false" targetId="fcb6-2503-af40-5e72" primary="false"/><categoryLink id="f23d-0699-c523-bda5" name="FC · Sacred Forge Walkers" hidden="false" targetId="52f6-34f0-629a-266e" primary="false"/><categoryLink id="28bd-6540-8834-899b" name="FC · Scouts &amp; Recon" hidden="false" targetId="9256-e70a-2cd2-8b45" primary="false"/><categoryLink id="2005-919d-2f72-39d9" name="FC · Siege Armor" hidden="false" targetId="84a9-2423-5dcb-b173" primary="false"/><categoryLink id="c722-5e0a-e6b7-af3a" name="FC · Siege Artillery" hidden="false" targetId="6718-fb81-5496-8416" primary="false"/><categoryLink id="e055-d969-bbcc-b32e" name="FC · Siege Assault" hidden="false" targetId="92bc-f579-7dc3-c5db" primary="false"/><categoryLink id="5edf-b248-6938-9aff" name="FC · Speeders &amp; Reconnaissance" hidden="false" targetId="3ca8-5dea-f094-c6e9" primary="false"/><categoryLink id="0d26-b3e5-df3a-2949" name="FC · Tactical Support" hidden="false" targetId="9d6e-0498-c734-3fe4" primary="false"/><categoryLink id="959e-588a-76b7-1b56" name="FC · Veterans" hidden="false" targetId="7560-57c6-6880-4a63" primary="false"/></categoryLinks></forceEntry></forceEntries>
</gameSystem>
