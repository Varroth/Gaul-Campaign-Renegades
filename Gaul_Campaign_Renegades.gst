<?xml version='1.0' encoding='utf-8'?>
<gameSystem xmlns="http://www.battlescribe.net/schema/gameSystemSchema" id="0408-b3dc-97f0-53dc" name="Gaul Campaign: Renegades" revision="15" battleScribeVersion="2.03">
  <costTypes>
    <costType id="0246-3343-a75c-5ffa" name="pts" defaultCostLimit="-1.0" hidden="false" />
    <costType id="6c3b-5f19-3bc2-5dbb" name="DP" defaultCostLimit="3.0" hidden="false" />
  </costTypes>
  <profileTypes>
    <profileType id="0cb1-7394-fb88-5322" name="Unit">
      <characteristicTypes>
        <characteristicType id="8ffa-8367-2184-5557" name="M" />
        <characteristicType id="c2bc-ad63-c63b-5cea" name="T" />
        <characteristicType id="f078-5176-43c6-5f6a" name="Sv" />
        <characteristicType id="ecdc-11e1-15d1-5780" name="W" />
        <characteristicType id="2bb6-cceb-9d3f-5f47" name="Ld" />
        <characteristicType id="6bb9-f7e0-3ec4-5517" name="OC" />
      <characteristicType name="Invulnerable" id="fcc9-7d25-7e12-9146" /></characteristicTypes>
    </profileType>
    <profileType id="bd5c-f804-35b5-510d" name="Ability">
      <characteristicTypes>
        <characteristicType id="4c71-0d90-3b92-5cec" name="Description" />
      </characteristicTypes>
    </profileType>
    <profileType id="a4f5-4674-06d7-5496" name="Weapon">
      <characteristicTypes>
        <characteristicType id="8aa7-21a6-b6c1-50e6" name="Range" />
        <characteristicType id="1df3-e803-7074-57ce" name="A" />
        <characteristicType id="a16c-0b6c-2681-5f8f" name="BS/WS" />
        <characteristicType id="846d-1dce-303c-5c75" name="S" />
        <characteristicType id="91f2-51a2-9429-5a60" name="AP" />
        <characteristicType id="14cd-2ade-2ccc-5c11" name="D" />
        <characteristicType id="0f05-4353-204c-511f" name="Traits" />
      </characteristicTypes>
    </profileType>
  </profileTypes>
  <categoryEntries>
    <categoryEntry id="b411-6717-d966-5c6d" name="Command" hidden="false" />
    <categoryEntry id="ec2c-68bb-bfbc-5ee3" name="Battleline" hidden="false" />
    <categoryEntry id="521d-dd50-6a49-58fb" name="Infantry" hidden="false" />
    <categoryEntry id="a7ac-6dda-f2f1-5ba4" name="Elites" hidden="false" />
    <categoryEntry id="c317-a497-01c6-5b78" name="Terminators" hidden="false" />
    <categoryEntry id="2a7b-0016-ba81-5ad6" name="Jump Infantry" hidden="false" />
    <categoryEntry id="bf60-94d3-7c97-5f42" name="Mounted" hidden="false" />
    <categoryEntry id="93a3-7ba9-2915-5ea2" name="Mortal Auxilia" hidden="false" />
    <categoryEntry id="930f-f4e6-1451-52ba" name="Dreadnoughts" hidden="false" />
    <categoryEntry id="693a-223d-bdae-5cbb" name="Vehicles" hidden="false" />
    <categoryEntry id="9856-3547-9660-54c2" name="Transports" hidden="false" />
    <categoryEntry id="6be8-bd06-032f-5209" name="Aircraft" hidden="false" />
    <categoryEntry id="4a72-54d4-f63a-5086" name="Artillery" hidden="false" />
    <categoryEntry id="b703-ed42-a968-5cce" name="Daemon Engines" hidden="false" />
    <categoryEntry id="471b-b5c6-68a0-523c" name="Khorne Allies" hidden="false"><constraints><constraint id="6d33efc5-a834-459e" type="max" field="0246-3343-a75c-5ffa" scope="roster" value="500" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" /></constraints><modifiers><modifier type="set" field="6d33efc5-a834-459e" value="250"><conditions><condition type="atLeast" value="1" field="selections" scope="roster" childId="b5e1b5c6-826e-48dd" shared="true" includeChildSelections="true" includeChildForces="true" /></conditions></modifier></modifiers></categoryEntry>
    <categoryEntry id="2962-6989-212f-598d" name="Lost Cohort" hidden="false"><constraints><constraint id="5fb20465-2d7f-49e5" type="max" field="selections" scope="roster" value="2" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true" /></constraints></categoryEntry>
    <categoryEntry id="3c17-c261-4038-5fcc" name="Detachments" hidden="false"><constraints><constraint field="selections" scope="force" value="4" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="5093-b84b-0ec5-5181" type="max" /><constraint field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="53ad-756a-e210-589f" type="min" /></constraints></categoryEntry>
    <categoryEntry id="40b7-29b0-a885-5757" name="Enhancements" hidden="false" />
    <categoryEntry id="9bc4-2501-1ea8-5f22" name="Muster Settings" hidden="false"><constraints><constraint id="3f4ebc3c-5ba2-461e-81a6-6a561ac06f4b" type="max" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true" /></constraints></categoryEntry>
    <categoryEntry id="b9f3-c313-59f0-5cef" name="Force Dispositions" hidden="false"><constraints><constraint id="bee1fe7f-89cc-40d6-a168-28d4f8f8a166" type="max" field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="true" /></constraints></categoryEntry>
    <categoryEntry id="524e-6fc1-14f9-5aa1" name="Configuration Tools" hidden="false" />
  <categoryEntry id="adbd-c48e-4b21-0002" name="Specialists" hidden="false" /><categoryEntry id="adbd-c48e-4b21-0003" name="Vehicles &amp; Support" hidden="false" /><categoryEntry id="adbd-c48e-4b21-a001" name="ASTARTES" hidden="false" /><categoryEntry id="adbd-c48e-4b21-a002" name="DIRECTORATE" hidden="false" /><categoryEntry id="adbd-c48e-4b21-a003" name="CULTISTS" hidden="false" /><categoryEntry id="b9b4-bb20-7903-f50e" name="Aerial Aces" hidden="false" /><categoryEntry id="237f-1a28-dc2b-753b" name="Aircraft &amp; Gunships" hidden="false" /><categoryEntry id="5b89-f231-abc9-9294" name="Armored Transports" hidden="false" /><categoryEntry id="85e4-2c59-f869-fd94" name="Assault Infantry" hidden="false" /><categoryEntry id="468e-98fe-33b9-74ff" name="Automata" hidden="false" /><categoryEntry id="adb6-d85c-dfb3-69ed" name="Battle Tanks" hidden="false" /><categoryEntry id="6d1a-80e9-0be4-0c2e" name="Battleline" hidden="false" /><categoryEntry id="70f4-8323-e145-4b4b" name="Bikes &amp; Jetbikes" hidden="false" /><categoryEntry id="a4bf-93d3-cebe-53ac" name="Chapter Command" hidden="false" /><categoryEntry id="2e98-8db1-b592-bebd" name="Character" hidden="false" /><categoryEntry id="7d07-115c-5f16-4c3b" name="Combat Engineers" hidden="false" /><categoryEntry id="7855-099c-f53c-d1e7" name="Contained Daemon Engines" hidden="false" /><categoryEntry id="a75f-1881-2e1a-697a" name="Dreadnoughts &amp; Living Masters" hidden="false" /><categoryEntry id="10d0-b638-38e6-f957" name="Drop Assault" hidden="false" /><categoryEntry id="4184-1d40-9d16-5a7a" name="Elite Siege Infantry" hidden="false" /><categoryEntry id="9198-67a8-0931-f114" name="Elite Wardens" hidden="false" /><categoryEntry id="ba92-31ee-3264-a18e" name="Frostbound Auxilia" hidden="false" /><categoryEntry id="e5e4-dd08-6ce4-34b7" name="Frozen Cogs" hidden="false" /><categoryEntry id="1186-3015-8b1c-a8a3" name="Harmonic Conclave" hidden="false" /><categoryEntry id="df1d-4be3-b832-eddc" name="Heavy Support" hidden="false" /><categoryEntry id="d640-7a85-a199-c350" name="Infantry" hidden="false" /><categoryEntry id="7a83-5343-b20a-173e" name="Melee Shock" hidden="false" /><categoryEntry id="994c-8bb9-1d19-a104" name="Named Characters" hidden="false" /><categoryEntry id="875f-19bf-1f26-b617" name="Relic Super-heavy Vehicles" hidden="false" /><categoryEntry id="fcb6-2503-af40-5e72" name="Sacred Forge Support" hidden="false" /><categoryEntry id="52f6-34f0-629a-266e" name="Sacred Forge Walkers" hidden="false" /><categoryEntry id="9256-e70a-2cd2-8b45" name="Scouts &amp; Recon" hidden="false" /><categoryEntry id="84a9-2423-5dcb-b173" name="Siege Armor" hidden="false" /><categoryEntry id="6718-fb81-5496-8416" name="Siege Artillery" hidden="false" /><categoryEntry id="92bc-f579-7dc3-c5db" name="Siege Assault" hidden="false" /><categoryEntry id="3ca8-5dea-f094-c6e9" name="Speeders &amp; Reconnaissance" hidden="false" /><categoryEntry id="9d6e-0498-c734-3fe4" name="Tactical Support" hidden="false" /><categoryEntry id="0a66-2bc3-4792-5c78" name="Terminator" hidden="false" /><categoryEntry id="7560-57c6-6880-4a63" name="Veterans" hidden="false" /><categoryEntry id="c1bd73c6-6a54-5bc3-ad26-514cbbbf90f6" name="Characters" hidden="false" /><categoryEntry id="124f46d4-4b66-58f3-ab79-949883ef8f65" name="Dreadnoughts &amp; Automata" hidden="false" /><categoryEntry id="f753b06d-12da-58ef-a3d3-3284910c5fa6" name="Auxiliaries" hidden="false" /><categoryEntry id="7fd0bc5d-4c25-5bd2-b4b6-a24999d47fe1" name="Silver Tempests" hidden="false" /><categoryEntry id="946fe999-f47e-59a0-bad1-701f4a973770" name="Army Configuration" hidden="false" /><categoryEntry id="dae8ec9a-f821-53bc-b6eb-794310db1e11" name="Infantry &amp; Elites" hidden="false" /><categoryEntry id="9feb91b4-eeed-5f5f-8ca8-4ad8caa4ca7c" name="Vehicles &amp; Artillery" hidden="false" /><categoryEntry id="22b28b7b-905e-51c8-8590-a8e5f503e56f" name="Auxiliaries &amp; Allies" hidden="false" /></categoryEntries>
  <forceEntries>
    <forceEntry id="73a9-6482-df85-55c4" name="Infernal Warriors Muster" hidden="false">
      <categoryLinks>
        <categoryLink id="0352845a-a8b5-5517-829d-b64b3a1c6051" name="Army Configuration" targetId="946fe999-f47e-59a0-bad1-701f4a973770" hidden="false" primary="false" /><categoryLink id="29d2ef8e-5418-5a02-b69e-0bb96d1a6a27" name="Characters" targetId="c1bd73c6-6a54-5bc3-ad26-514cbbbf90f6" hidden="false" primary="false" /><categoryLink id="bec9-e84b-e7d4-52e8" name="Battleline" hidden="false" targetId="ec2c-68bb-bfbc-5ee3" primary="false" />
        <categoryLink id="48f94b30-ca5e-5848-9d6f-494880f97998" name="Infantry &amp; Elites" targetId="dae8ec9a-f821-53bc-b6eb-794310db1e11" hidden="false" primary="false" /><categoryLink id="4892-9cac-0368-5f7a" name="Lost Cohort" hidden="false" targetId="2962-6989-212f-598d" primary="false">
          <constraints><constraint field="selections" scope="force" value="2" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" id="bf50-49c8-01dd-51e6" type="max" /></constraints>
        </categoryLink>
        <categoryLink id="5e7a-a931-61b3-58c4" name="Dreadnoughts" hidden="false" targetId="930f-f4e6-1451-52ba" primary="false" />
        <categoryLink id="723f611c-c2c2-54a8-bfdd-f8664cd03623" name="Vehicles &amp; Artillery" targetId="9feb91b4-eeed-5f5f-8ca8-4ad8caa4ca7c" hidden="false" primary="false" /><categoryLink id="88ea-6ee8-a69f-5e11" name="Aircraft" hidden="false" targetId="6be8-bd06-032f-5209" primary="false" />
        <categoryLink id="8519-9461-bd3d-52e5" name="Daemon Engines" hidden="false" targetId="b703-ed42-a968-5cce" primary="false" />
        <categoryLink id="eab5a0df-cb16-575d-9ea9-f5c2260b6757" name="Auxiliaries &amp; Allies" targetId="22b28b7b-905e-51c8-8590-a8e5f503e56f" hidden="false" primary="false" /></categoryLinks>
    </forceEntry>
  <forceEntry id="ada1-e202-6a1d-ecad" name="Abandoned Dead Task Force" hidden="false"><categoryLinks><categoryLink id="ad7f-0000-fcce-2026" name="Command" hidden="false" targetId="b411-6717-d966-5c6d" primary="false" /><categoryLink id="ad7f-0001-fcce-2026" name="Battleline" hidden="false" targetId="ec2c-68bb-bfbc-5ee3" primary="false" /><categoryLink id="ad7f-0002-fcce-2026" name="Specialists" hidden="false" targetId="adbd-c48e-4b21-0002" primary="false" /><categoryLink id="ad7f-0003-fcce-2026" name="Vehicles &amp; Support" hidden="false" targetId="adbd-c48e-4b21-0003" primary="false" /><categoryLink id="ad7f-0004-fcce-2026" name="ASTARTES" hidden="false" targetId="adbd-c48e-4b21-a001" primary="false" /><categoryLink id="ad7f-0005-fcce-2026" name="DIRECTORATE" hidden="false" targetId="adbd-c48e-4b21-a002" primary="false" /><categoryLink id="ad7f-0006-fcce-2026" name="CULTISTS" hidden="false" targetId="adbd-c48e-4b21-a003" primary="false" /></categoryLinks></forceEntry><forceEntry id="5513-326d-9459-9678" name="Frozen Cogs Expeditionary Force" hidden="false"><categoryLinks><categoryLink id="0c0ebfe2-0890-587f-8ad7-f12519a1aeaf" name="Characters" targetId="c1bd73c6-6a54-5bc3-ad26-514cbbbf90f6" hidden="false" primary="false" /><categoryLink id="7b3c9e71-0a62-5f92-9281-c55e4cda7797" name="Battleline" targetId="6d1a-80e9-0be4-0c2e" hidden="false" primary="false" /><categoryLink id="c775e9c1-b7c1-589f-947d-f9b5e62ddb54" name="Infantry" targetId="d640-7a85-a199-c350" hidden="false" primary="false" /><categoryLink id="f86eb22f-7e17-5a0c-be0d-b15c73ce63dc" name="Dreadnoughts &amp; Automata" targetId="124f46d4-4b66-58f3-ab79-949883ef8f65" hidden="false" primary="false" /><categoryLink id="01be00c3-fd0b-5597-809a-db31064725ec" name="Vehicles" targetId="693a-223d-bdae-5cbb" hidden="false" primary="false" /><categoryLink id="ab01d338-9ebc-565e-912b-0b21a68ea0d2" name="Aircraft" targetId="6be8-bd06-032f-5209" hidden="false" primary="false" /><categoryLink id="8e0323b5-d4d7-5adb-882a-f26796ffced0" name="Daemon Engines" targetId="b703-ed42-a968-5cce" hidden="false" primary="false" /><categoryLink id="2894ed8d-2f32-52a9-a2ef-be35f02add65" name="Auxiliaries" targetId="f753b06d-12da-58ef-a3d3-3284910c5fa6" hidden="false" primary="false" /><categoryLink id="7a559cf1-5f45-578e-bcab-2cc5265d2aef" name="Silver Tempests" targetId="7fd0bc5d-4c25-5bd2-b4b6-a24999d47fe1" hidden="false" primary="false" /></categoryLinks></forceEntry></forceEntries>
</gameSystem>