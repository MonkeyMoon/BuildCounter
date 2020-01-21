// Written by @valryon for MONKEYMOON
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace MM.Utils
{
    [CreateAssetMenu(fileName = "BuildVersion", menuName = "Build Version")]
    public class BuildVersionData : ScriptableObject
    {
        public int major;
        public int minor;
        public int patch;
        public string commit_hash;

        public override string ToString()
        {
            return string.Format("{0}.{1}.{2}", major, minor, patch);
        }

        public string ToStringWithCommit()
        {
            return ToString() + " " + commit_hash;
        }
    }
}

