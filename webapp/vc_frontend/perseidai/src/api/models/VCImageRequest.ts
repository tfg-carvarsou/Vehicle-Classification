/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VCImageModelEnum } from './VCImageModelEnum';
export type VCImageRequest = {
    /**
     * The ML model for classifying vehicles
     *
     * * `EfficientNetB1` - EFFNETB1
     * * `YOLOv8s-cls` - YOLOV8SCLS
     */
    model?: VCImageModelEnum;
    /**
     * The image file to be uploaded
     */
    image: Blob;
};

